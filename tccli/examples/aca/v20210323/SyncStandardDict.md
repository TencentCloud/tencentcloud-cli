**Example 1: 同步给药频次**

同步给药频次

Input: 

```
tccli aca SyncStandardDict --cli-unfold-argument  \
    --Header.HospitalId 001 \
    --Header.Token tai.4d563878587a67774d44417a4e544d344e413d3d.1959c3405c614d709babfad5e1b79d54 \
    --Data.HospitalId 001 \
    --Data.DictType 1 \
    --Data.Dicts.0.FreqCode qid \
    --Data.Dicts.0.FreqName 一日三次 \
    --Data.Dicts.0.Disable 0
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Message": "success",
        "RequestId": "77f9c09c-8db0-40e9-8293-d4620e82cc9b"
    }
}
```

