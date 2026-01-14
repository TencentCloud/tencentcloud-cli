**Example 1: 调用请求示例**



Input: 

```
tccli hunyuan Convert3DFormat --cli-unfold-argument  \
    --Format STL \
    --File3D https://cos.ap-guangzhou.tencentcos.cn/xxx.zip
```

Output: 
```
{
    "Response": {
        "RequestId": "78722611-9e48-43fd-8e27-2672bae39d7b",
        "ResultFile3D": "https://cos.ap-guangzhou.tencentcos.cn/xxx.stl"
    }
}
```

