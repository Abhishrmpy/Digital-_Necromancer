# backend/test_file_processor.py
import os
import sys
from pathlib import Path

# Add current directory to path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from core.file_processor import file_processor

def test_file_processor():
    print("🔍 Testing File Processor...")
    print(f"📁 Current directory: {os.getcwd()}")
    
    # Test with our test_files directory
    test_folder = "test_files"
    print(f"🔍 Looking for folder: '{test_folder}'")
    
    if os.path.exists(test_folder):
        print(f"✅ Folder found! Contents: {os.listdir(test_folder)}")
    else:
        print(f"❌ Folder '{test_folder}' not found.")
        return
    
    try:
        # Test the file processor
        processed_files = file_processor.process_directory(test_folder)
        
        print("✅ File processor test successful!")
        print(f"📁 Processed {len(processed_files)} files:")
        
        for file in processed_files:
            status = "✅" if file.success else "❌"
            print(f"  {status} {file.filename} ({file.file_type})")
            if file.error:
                print(f"    Error: {file.error}")
            else:
                print(f"    Content length: {len(file.content)} characters")
        
        # Test combining content
        combined = file_processor.get_combined_content(processed_files)
        print(f"\n📄 Combined content length: {len(combined)} characters")
        print(f"📄 Preview: {combined[:200]}...")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_file_processor()