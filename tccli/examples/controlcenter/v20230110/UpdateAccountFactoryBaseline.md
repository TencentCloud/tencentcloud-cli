**Example 1: 示例**

批量更新/增加用户基线配置

Input: 

```
tccli controlcenter UpdateAccountFactoryBaseline --cli-unfold-argument  \
    --Name default \
    --BaselineConfigItems.0.Identifier ACS-BP_ACCOUNT_FACTORY_ACCOUNT_CONTACT \
    --BaselineConfigItems.0.Configuration {"Contacts":[{"Name":"dest","Email":"ia@22.com","Mobile":"12345678910","Position":"Technical Director"}]}
```

Output: 
```
{
    "Response": {
        "RequestId": "748eabd0-5d58-40a6-85e3-26d74c3397d4"
    }
}
```

