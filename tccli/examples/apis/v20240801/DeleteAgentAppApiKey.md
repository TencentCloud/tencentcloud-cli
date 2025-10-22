**Example 1: 删除app的apiKey**

删除app的apiKey

Input: 

```
tccli apis DeleteAgentAppApiKey --cli-unfold-argument  \
    --ID aga-71702335 \
    --InstanceID ins-e6fbc9b9 \
    --Index 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-71702335"
        },
        "RequestId": "0c61b0f7-5467-440d-b7ec-7f20f798a69e"
    }
}
```

