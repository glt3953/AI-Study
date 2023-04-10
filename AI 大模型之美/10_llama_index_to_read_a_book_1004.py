
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
from llama_index.readers.file.base import DEFAULT_FILE_EXTRACTOR, ImageParser
from llama_index.response.notebook_utils import display_response, display_image
from llama_index.indices.query.query_transform.base import ImageOutputQueryTransform

image_parser = ImageParser(keep_image=True, parse_text=True)
file_extractor = DEFAULT_FILE_EXTRACTOR
file_extractor.update(
{
    ".jpg": image_parser,
    ".png": image_parser,
    ".jpeg": image_parser,
})

# NOTE: we add filename as metadata for all documents
filename_fn = lambda filename: {'file_name': filename}

receipt_reader = SimpleDirectoryReader(
    input_dir='./data/receipts',
    file_extractor=file_extractor,
    file_metadata=filename_fn,
)
receipt_documents = receipt_reader.load_data()

receipts_index = GPTSimpleVectorIndex.from_documents(receipt_documents)
#receipts_response = receipts_index.query(
#    'When was the last time I went to McDonald\'s and how much did I spend. \
#    Also show me the receipt from my visit.',
#    query_transform=ImageOutputQueryTransform(width=400)
#)
#
#display_response(receipts_response)

output_image = image_parser.parse_file('./data/receipts/1100-receipt.jpg')
print(output_image.text)
