# src/setup_and_test.py
"""
Setup script to verify that all components are working correctly
and run initial tests on the RAG pipeline.
"""

import os
import sys
from pathlib import Path

def check_requirements():
    """Check if all required files and directories exist."""
    required_paths = [
        "vector_store/faiss_index.bin",
        "vector_store/metadata.pkl",
        "data/filtered_complaints.csv"
    ]
    
    missing_paths = []
    for path in required_paths:
        if not os.path.exists(path):
            missing_paths.append(path)
    
    if missing_paths:
        print("❌ Missing required files:")
        for path in missing_paths:
            print(f"   - {path}")
        print("\nPlease ensure you have completed Tasks 1 and 2 first.")
        return False
    else:
        print("✅ All required files found!")
        return True

def test_rag_pipeline():
    """Test the RAG pipeline with sample questions."""
    try:
        from rag_pipeline import RAGPipeline
        
        print("\n🧪 Testing RAG Pipeline...")
        rag = RAGPipeline()
        
        test_questions = [
            "What are credit card issues?",
            "Problems with personal loans?",
            "BNPL complaints?"
        ]
        
        for question in test_questions:
            print(f"\nTesting: {question}")
            response = rag.answer_question(question)
            print(f"✅ Response generated: {len(response['answer'])} characters")
            print(f"📊 Sources retrieved: {response['num_sources']}")
        
        print("\n✅ RAG Pipeline test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ RAG Pipeline test failed: {str(e)}")
        return False

def run_quick_evaluation():
    """Run a quick evaluation of the system."""
    try:
        from rag_pipeline import RAGPipeline, RAGEvaluator
        
        print("\n📊 Running Quick Evaluation...")
        rag = RAGPipeline()
        evaluator = RAGEvaluator(rag)
        
        # Run evaluation on first 3 questions only
        questions = evaluator.create_evaluation_questions()[:3]
        
        results = []
        for q_data in questions:
            response = rag.answer_question(q_data['question'])
            evaluation = evaluator.evaluate_response_quality(
                q_data['question'], 
                response, 
                q_data['expected_elements']
            )
            results.append(evaluation['overall_score'])
            print(f"✅ {q_data['question'][:50]}... Score: {evaluation['overall_score']}/5")
        
        avg_score = sum(results) / len(results)
        print(f"\n📈 Average Score: {avg_score:.2f}/5")
        
        return True
        
    except Exception as e:
        print(f"❌ Evaluation failed: {str(e)}")
        return False

def main():
    """Main setup and testing function."""
    print("🚀 CrediTrust Complaint Analyzer - Setup & Testing")
    print("=" * 55)
    
    # Check requirements
    if not check_requirements():
        return
    
    # Test RAG pipeline
    if not test_rag_pipeline():
        return
    
    # Run quick evaluation
    if not run_quick_evaluation():
        return
    
    print("\n🎉 All tests passed! Your system is ready to use.")
    print("\n🚀 To start the chat interface, run:")
    print("   python app.py")

if __name__ == "__main__":
    main()