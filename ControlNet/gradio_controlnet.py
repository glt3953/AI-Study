from gradio_client import Client

client = Client("https://b05c-34-83-211-102.ngrok-free.app/")
result = client.predict(
                "Normal_BAE",    # str  in 'Preprocessor' Radio component,Normal_BAE,SoftEdge_PIDI,SoftEdge_HED
#                "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",    # str (filepath or URL to image) in 'parameter_5' Image component
                "person-leaves.png", #IMG_8298.JPG, 证件照.jpg
                "a boy made of flowers",    # str  in 'Prompt' Textbox component
                "best quality",    # str  in 'Added Prompt' Textbox component
                "lowres, bad anatomy, bad hands, cropped, worst quality",    # str  in 'Negative Prompt' Textbox component
                1,    # int | float (numeric value between 1 and 12) in 'Images' Slider component
                512,    # int | float (numeric value between 256 and 768) in 'Image Resolution' Slider component
                512,    # int | float (numeric value between 128 and 1024) in 'Preprocessor Resolution' Slider component
                20,    # int | float (numeric value between 1 and 100) in 'Steps' Slider component
                False,    # bool  in 'Guess Mode' Checkbox component
                1,    # int | float (numeric value between 0.0 and 2.0) in 'Control Strength' Slider component
                9,    # int | float (numeric value between 0.1 and 30.0) in 'Guidance Scale' Slider component
                12345,    # int | float (numeric value between -1 and 2147483647) in 'Seed' Slider component
                1,    # int | float (numeric value between 0.0 and 1.0) in 'DDIM ETA' Slider component
#                False,    # bool  in 'Safe' Checkbox component
                fn_index=0
)
print(result)
