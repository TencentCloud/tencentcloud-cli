**Example 1: 创建prompt任务**

创建prompt任务

Input: 

```
tccli hai CreateMuskPrompt --cli-unfold-argument  \
    --WorkgroupId 4a3f3be9-f35b-40bf-b6bb-2af812dd63cb \
    --WorkflowId wf-b9dbb48a-f4cd-40f3-9a68-2af4c78d31a7 \
    --PromptParams {"6":{"inputs":{"text":"cute anime girl with massive fluffy fennec ears and a big fluffy tail blonde messy long hair blue eyes wearing a maid outfit with a long black gold leaf pattern dress and a white apron mouth open holding a fancy black forest cake with candles on top in the kitchen of an old dark Victorian mansion lit by candlelight with a bright window to the foggy forest and very expensive stuff everywhere","clip":["11",0]},"class_type":"CLIPTextEncode","_meta":{"title":"CLIP Text Encode (Positive Prompt)"}},"8":{"inputs":{"samples":["13",0],"vae":["10",0]},"class_type":"VAEDecode","_meta":{"title":"VAE解码"}},"9":{"inputs":{"filename_prefix":"ComfyUI","images":["8",0]},"class_type":"SaveImage","_meta":{"title":"保存图像"}},"10":{"inputs":{"vae_name":"ae.sft"},"class_type":"VAELoader","_meta":{"title":"加载VAE"}},"11":{"inputs":{"clip_name1":"t5xxl_fp8_e4m3fn.safetensors","clip_name2":"clip_l.safetensors","type":"flux"},"class_type":"DualCLIPLoader","_meta":{"title":"双CLIP加载器"}},"12":{"inputs":{"unet_name":"flux1-dev-fp8.safetensors","weight_dtype":"fp8_e4m3fn"},"class_type":"UNETLoader","_meta":{"title":"加载扩散模型"}},"13":{"inputs":{"noise":["25",0],"guider":["22",0],"sampler":["16",0],"sigmas":["17",0],"latent_image":["27",0]},"class_type":"SamplerCustomAdvanced","_meta":{"title":"自定义采样器（高级）"}},"16":{"inputs":{"sampler_name":"euler"},"class_type":"KSamplerSelect","_meta":{"title":"K采样器选择"}},"17":{"inputs":{"scheduler":"simple","steps":20,"denoise":1,"model":["30",0]},"class_type":"BasicScheduler","_meta":{"title":"基本调度器"}},"22":{"inputs":{"model":["30",0],"conditioning":["26",0]},"class_type":"BasicGuider","_meta":{"title":"基本引导器"}},"25":{"inputs":{"noise_seed":317016131367339},"class_type":"RandomNoise","_meta":{"title":"随机噪声"}},"26":{"inputs":{"guidance":3.5,"conditioning":["6",0]},"class_type":"FluxGuidance","_meta":{"title":"Flux引导"}},"27":{"inputs":{"width":1024,"height":1024,"batch_size":1},"class_type":"EmptySD3LatentImage","_meta":{"title":"空SD3潜空间图像"}},"30":{"inputs":{"max_shift":1.15,"base_shift":0.5,"width":1024,"height":1024,"model":["12",0]},"class_type":"ModelSamplingFlux","_meta":{"title":"模型采样Flux"}}}
```

Output: 
```
{
    "Response": {
        "PromptId": "edc6e6ec-072c-41dd-8672-c956b739fd31",
        "RequestId": "840728c5-4abb-4eb5-b469-a304631693f9"
    }
}
```

