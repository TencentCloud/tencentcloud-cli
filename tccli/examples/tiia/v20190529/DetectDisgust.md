**Example 1: 恶心检测接口调用成功**



Input: 

```
tccli tiia DetectDisgust --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg
```

Output: 
```
{
    "Response": {
        "Confidence": 0.98,
        "Type": "蛇",
        "RequestId": "40afdbfc-be4c-4530-bb1a-3f1683b05dba"
    }
}
```

