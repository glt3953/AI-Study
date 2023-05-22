import { client } from "@gradio/client";

async function run() {

    const response_0 = await fetch("证件照.jpg");
    const exampleImage = await response_0.blob();
                        
    const app = await client("https://6af0-34-83-211-102.ngrok-free.app/");
    const result = await app.predict(0, [
                "SoftEdge_PIDI", // string  in 'Preprocessor' Radio component,SoftEdge_PIDI,SoftEdge_HED
                exampleImage,     // blob in 'parameter_5' Image component
                "oil painting of handsome young man, wear a pair of black-rimmed glasses, masterpiece", // string  in 'Prompt' Textbox component
                "best quality", // string  in 'Added Prompt' Textbox component
                "lowres, bad anatomy, bad hands, cropped, worst quality", // string  in 'Negative Prompt' Textbox component
                1, // number (numeric value between 1 and 12) in 'Images' Slider component
                512, // number (numeric value between 256 and 768) in 'Image Resolution' Slider component
                512, // number (numeric value between 128 and 1024) in 'Preprocessor Resolution' Slider component
                20, // number (numeric value between 1 and 100) in 'Steps' Slider component
                false, // boolean  in 'Guess Mode' Checkbox component
                1, // number (numeric value between 0.0 and 2.0) in 'Control Strength' Slider component
                9, // number (numeric value between 0.1 and 30.0) in 'Guidance Scale' Slider component
                12345, // number (numeric value between -1 and 2147483647) in 'Seed' Slider component
                1, // number (numeric value between 0.0 and 1.0) in 'DDIM ETA' Slider component
                false, // boolean  in 'Safe' Checkbox component
    ]);

    console.log(result?.data);
}

run();
