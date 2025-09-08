# backend/debug_ai.py
import os
import sys
from pathlib import Path

# Add current directory to path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

def test_hf_token():
    print("🔍 Checking HF_TOKEN...")
    hf_token = os.environ.get("HF_TOKEN")
    print(f"   HF_TOKEN value: {hf_token}")
    print(f"   HF_TOKEN length: {len(hf_token) if hf_token else 0}")
    print(f"   HF_TOKEN starts with 'hf_': {hf_token.startswith('hf_') if hf_token else False}")
    return hf_token

def test_huggingface_import():
    print("\n🔍 Testing huggingface_hub import...")
    try:
        from huggingface_hub import InferenceClient
        print("   ✅ huggingface_hub imported successfully")
        return InferenceClient
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return None

def test_inference_client(hf_token, InferenceClient):
    print("\n🔍 Testing InferenceClient creation...")
    try:
        client = InferenceClient(provider="together", api_key=hf_token)
        print("   ✅ InferenceClient created successfully")
        return client
    except Exception as e:
        print(f"   ❌ Client creation failed: {e}")
        return None

def test_api_call(client):
    print("\n🔍 Testing API call...")
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": "Hello, are you working?"}],
            max_tokens=50
        )
        print("   ✅ API call successful!")
        print(f"   Response: {completion.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"   ❌ API call failed: {e}")
        return False

def main():
    print("🚀 Starting AI Client Diagnostic...")
    
    # Test 1: Check HF_TOKEN
    hf_token = test_hf_token()
    if not hf_token:
        print("\n❌ HF_TOKEN not found. Please set it with: set HF_TOKEN=your_token")
        return
    
    # Test 2: Check import
    InferenceClient = test_huggingface_import()
    if not InferenceClient:
        return
    
    # Test 3: Check client creation
    client = test_inference_client(hf_token, InferenceClient)
    if not client:
        return
    
    # Test 4: Check API call
    success = test_api_call(client)
    
    if success:
        print("\n🎉 All tests passed! The AI client should work.")
    else:
        print("\n❌ API call failed. Check your HF_TOKEN or network connection.")

if __name__ == "__main__":
    main()