**Example 1: TAV公有云查**



Input: 

```
tccli tav ScanFileHash --cli-unfold-argument  \
    --Key d12790cf44382a3c15e4e8c63e41e74d \
    --Md5s 0f600011f6abb02f6a117e1efb952a3c \
    --WithCategory 0 \
    --SensitiveLevel 10
```

Output: 
```
{
    "Response": {
        "Status": 200,
        "Info": "scan success",
        "Data": "md5:0f600011f6abb02f6a117e1efb952a3c,return_state:1,virus_state:2,virus_name:Win32.Trojan.Agent.tkxh|",
        "RequestId": "00f29851-2408-4818-b66c-3b2d2ba4196f"
    }
}
```

