from gradio_client import Client

client = Client("https://54ac-34-124-135-235.ngrok-free.app/")
result = client.predict(
                "7e37f4573f9c4847aaa502b79460cb7d.jpeg", #IMG_8298.JPG, 证件照.jpg, 22_head_big.png, IMG_7111_head.png, IMG_3512_head.png
                "Pixar style of handsome young man, masterpiece",    # str  in 'Prompt' Textbox component
                "best quality, extremely detailed",    # str  in 'Added Prompt' Textbox component
                "longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality",    # str  in 'Negative Prompt' Textbox component
                1,    # int | float (numeric value between 1 and 12) in 'Images' Slider component
                512,    # int | float (numeric value between 256 and 768) in 'Image Resolution' Slider component
                512,    # int | float (numeric value between 128 and 1024) in 'Preprocessor Resolution' Slider component
                20,    # int | float (numeric value between 1 and 100) in 'Steps' Slider component
                False,    # bool  in 'Guess Mode' Checkbox component
                1,    # int | float (numeric value between 0.0 and 2.0) in 'Control Strength' Slider component
                9,    # int | float (numeric value between 0.1 and 30.0) in 'Guidance Scale' Slider component
                89834816,    # int | float (numeric value between -1 and 2147483647) in 'Seed' Slider component
                1,    # int | float (numeric value between 0.0 and 1.0) in 'DDIM ETA' Slider component
                fn_index=0
)
print(result)
