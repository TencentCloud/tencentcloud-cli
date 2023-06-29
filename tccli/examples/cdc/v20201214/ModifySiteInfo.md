**Example 1: 修改机房信息**

修改机房信息

Input: 

```
tccli cdc ModifySiteInfo --cli-unfold-argument  \
    --SiteId site-xxxx \
    --Name new_name \
    --Description new_description \
    --Note new_note \
    --Country China \
    --Province Guangdong \
    --City Shenzhen \
    --PostalCode 14353 \
    --AddressLine 腾讯滨海大厦
```

Output: 
```
{
    "Response": {
        "RequestId": "3ceeecd2-2f24-4b3f-81eb-346137682c3f"
    }
}
```

