**Example 1: 创建合同对比web页面**



Input: 

```
tccli ess CreateContractDiffTaskWebUrl --cli-unfold-argument  \
    --Operator.UserId yDw9iUUgyg36ykr3Ux4GQpt1FPWYQOZC \
    --SkipFileUpload True
```

Output: 
```
{
    "Response": {
        "RequestId": "s1748574341239597750",
        "TaskId": "",
        "WebUrl": "https://embed.qian.tencent.cn/contract-compare?embed=1&code=yDtthUUckpx9l14eUy8nTBEypH6h1yKt&channel=TENCENTCLOUD&embedType=CONTRACT_DIFF"
    }
}
```

**Example 2: 创建合同对比web页面 - 跳过文件上传确认页**



Input: 

```
tccli ess CreateContractDiffTaskWebUrl --cli-unfold-argument  \
    --Operator.UserId yDw9iUUgyg36ykr3Ux4GQpt1FPWYQOZC \
    --OriginalFileResourceId yDttXUUckpx90i17UxPpcHHE1VDpNJPW \
    --DiffFileResourceId yDttXUUckpx90i1xUxPpcHHyPdyqVErm \
    --SkipFileUpload True \
    --UserData QmFzZTY0IEJhc2U2NCA \
    --Tags.0.TagKey key1 \
    --Tags.0.TagValue value1
```

Output: 
```
{
    "Response": {
        "RequestId": "s1748937464610832514",
        "TaskId": "yDt31UUckpx91cypUyoAic6wP2oyarMN",
        "WebUrl": "https://embed.qian.tencent.cn/contract-compare?embed=1&code=yDt31UUckpx9196lUxKwEYgzw4fEWCom&channel=TENCENTCLOUD&embedType=CONTRACT_DIFF&businessType=TASK_ID&businessId=yDt31UUckpx91cypUyoAic6wP2oyarMN",
        "UserData": "QmFzZTY0IEJhc2U2NCA"
    }
}
```

