**Example 1: 获取用户安全组列表**

获取用户安全组列表

Input: 

```
tccli cloudhsm DescribeUsg --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --SearchWord sg-p9k0swj3	
```

Output: 
```
{
    "Response": {
        "RequestId": "251e4fb4-110a-4d3e-ac6c-cceff9672394",
        "SgList": [
            {
                "CreateTime": "2024-08-30 10:16:07",
                "SgId": "sg-p9k0swj3",
                "SgName": "放通22，80，443，3389端口和ICMP协议-2024083010155758656",
                "SgRemark": "公网放通云主机常用登录及web服务端口，内网全放通。"
            },
            {
                "CreateTime": "2024-02-02 16:53:18",
                "SgId": "sg-6tjv5yxb",
                "SgName": "default",
                "SgRemark": "System created security group"
            },
            {
                "CreateTime": "2022-09-18 11:24:11",
                "SgId": "sg-ro3eh7bb",
                "SgName": "放通22，80，443，3389端口和ICMP协议-2022091811240925063",
                "SgRemark": "公网放通云主机常用登录及web服务端口，内网全放通。"
            },
            {
                "CreateTime": "2022-02-10 14:24:04",
                "SgId": "sg-3qcokmyz",
                "SgName": "放通全部端口-2022021014240020071",
                "SgRemark": "暴露全部端口到公网和内网，有一定安全风险"
            }
        ],
        "TotalCount": 4
    }
}
```

