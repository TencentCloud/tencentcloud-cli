**Example 1: 关闭内容合规检测开关**

关闭指定域名的内容合规检测（SwitchType=6）

Input: 

```
tccli waf ModifyLLMStatus --cli-unfold-argument  \
    --Status False \
    --Domain example.com \
    --SwitchType 6 \
    --InstanceId waf_2kxtlbky01b3wceb
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Res": "Success"
    }
}
```

**Example 2: 开启大模型防护总开关**

开启指定域名的大模型防护总开关

Input: 

```
tccli waf ModifyLLMStatus --cli-unfold-argument  \
    --Status True \
    --Domain example.com \
    --SwitchType 1 \
    --InstanceId waf_2kxtlbky01b3wceb
```

Output: 
```
{
    "Response": {
        "RequestId": "086bade4-6f71-4b37-949d-ed472feb3d1e",
        "Res": "Success"
    }
}
```

