**Example 1: 批量创建Key**



Input: 

```
tccli clb CreateKeys --cli-unfold-argument  \
    --ModelRouterId cmr-jcxor1gp \
    --Keys.0.KeyName 批量创建Key测试 \
    --BudgetId budget-86mldfuv
```

Output: 
```
{
    "Response": {
        "CreatedKeys": [
            {
                "Key": "sk-W3BfTOx0ZWJ4llGNwbEZ81twh-2HxgwcFfED7fVychbNXZdTE-S0mHxdkKTHWk_q_bEJaAl8ykT0eJbgBdlsxZ5V23LtL3j0Pdx0bBxivg",
                "KeyId": "vkey-evbmx1m1",
                "KeyName": "批量创建Key测试"
            }
        ],
        "RequestId": "83e382d1-2823-4a87-b10a-896898d27f77"
    }
}
```

