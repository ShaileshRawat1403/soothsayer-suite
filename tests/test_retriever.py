# test_retriever.py

from tools.retriever import build_retriever_from_md
import os

# Set your markdown path (replace if needed)
TEST_MD = "input_docs/test_sample.md"

def run_test():
    if not os.path.exists(TEST_MD):
        with open(TEST_MD, "w") as f:
            f.write("# Test Doc\n\nThis is a test file.\n- Bullet 1\n- Bullet 2\n\n## Section\nText under section.")

    vectorstore, chunks = build_retriever_from_md(TEST_MD)

    print("Chunks:")
    for chunk in chunks:
        print("-", chunk[:60])

    if vectorstore:
        print("\nVectorstore built and ready for retrieval ✅")

if __name__ == "__main__":
    run_test()
