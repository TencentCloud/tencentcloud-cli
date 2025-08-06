**Example 1: 成功调用-任务完成**

成功调用查询任务接口，任务完成。

Input: 

```
tccli vclm DescribeVideoStylizationJob --cli-unfold-argument  \
    --JobId c5daf8f7077d41a69c13aab31a7164f3
```

Output: 
```
{
    "Response": {
        "JobId": "c5daf8f7077d41a69c13aab31a7164f3",
        "RequestId": "c048e3cf-79b3-4080-9892-15bb96a680e5",
        "ResultVideoUrl": "https://vcg-prod-xxx.cos.ap-guangzhou.tencentcos.cn/xxx.mp4",
        "StatusCode": "JobSuccess",
        "StatusMsg": "处理完成"
    }
}
```

