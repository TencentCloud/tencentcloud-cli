**Example 1: 封禁或解封项目**

封禁或解封项目及 Preset、Custom、Deployment 域名。

Input: 

```
tccli makers BlockProject --cli-unfold-argument  \
    --ZoneId zone-3vdi1u3iez9g \
    --ProjectId makers-gk6nldnxsolv \
    --Status Ban
```

Output: 
```
{
    "Response": {
        "RequestId": "ea3834ef-53cd-4fa0-8bea-5554ffb60d8e"
    }
}
```

