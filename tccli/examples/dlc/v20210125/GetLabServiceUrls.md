**Example 1: GetLabServiceUrls**

获取实验室webide 地址

Input: 

```
tccli dlc GetLabServiceUrls --cli-unfold-argument  \
    --Id raylab-20260530151529-r6av
```

Output: 
```
{
    "Response": {
        "ServiceUrls": [
            {
                "Key": "JUPYTER",
                "Value": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-bleurqnv/raylab-20260530151529-r6av/lab/jupyter"
            }
        ],
        "RequestId": "6bae38af-8688-4423-9b2a-f63d862f1d47"
    }
}
```

