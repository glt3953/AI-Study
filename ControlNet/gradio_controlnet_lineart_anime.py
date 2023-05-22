from gradio_client import Client

client = Client("https://6850-34-83-211-102.ngrok-free.app/")
result = client.predict(
                "Lineart_Anime",    # str  in 'Preprocessor' Radio component
                "anime3.jpg", #IMG_8298.JPG, 证件照.jpg
                "one girl, in classroom, white skirt, uniform, black hair, bag, blue eyes",    # str  in 'Prompt' Textbox component
                "masterpiece, best quality, ultra-detailed, illustration, disheveled hair",    # str  in 'Added Prompt' Textbox component
                "longbody, lowres, bad anatomy, bad hands, missing fingers, pubic hair,extra digit, fewer digits, cropped, worst quality, low quality",    # str  in 'Negative Prompt' Textbox component
                1,    # int | float (numeric value between 1 and 12) in 'Images' Slider component
                512,    # int | float (numeric value between 256 and 768) in 'Image Resolution' Slider component
                512,    # int | float (numeric value between 128 and 1024) in 'Preprocessor Resolution' Slider component
                20,    # int | float (numeric value between 1 and 100) in 'Steps' Slider component
                1,    # int | float (numeric value between 0.0 and 2.0) in 'Control Strength' Slider component
                9,    # int | float (numeric value between 0.1 and 30.0) in 'Guidance Scale' Slider component
                12345,    # int | float (numeric value between -1 and 2147483647) in 'Seed' Slider component
                1,    # int | float (numeric value between 0.0 and 1.0) in 'DDIM ETA' Slider component
                fn_index=0
)
print(result)
