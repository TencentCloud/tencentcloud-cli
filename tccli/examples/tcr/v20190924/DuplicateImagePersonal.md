**Example 1: 复制个人版仓库镜像tag**



Input: 

```
tccli tcr DuplicateImagePersonal --cli-unfold-argument  \
    --SrcImage dockerhub/test:1.0 \
    --DestImage dockerhub/test:2.0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "Digest": "sha256:b3e07cf570a86f5bd5c770e86ccbc2d1c2e79081b1b966332ba873a6d1c3481c"
        }
    }
}
```

