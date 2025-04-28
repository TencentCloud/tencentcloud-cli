**Example 1: 获取图片优化的配置**



Input: 

```
tccli cdn DescribeImageConfig --cli-unfold-argument  \
    --Domain test.tencent.com
```

Output: 
```
{
    "Response": {
        "WebpAdapter": {
            "Switch": "on"
        },
        "TpgAdapter": {
            "Switch": "on"
        },
        "GuetzliAdapter": {
            "Switch": "on"
        },
        "AvifAdapter": {
            "Switch": "on"
        },
        "RequestId": "29699aac-9898-4baf-b645-7cc31d972674"
    }
}
```

