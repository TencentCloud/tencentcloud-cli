**Example 1: 同步科室**

新增科室数据

Input: 

```
tccli aca SyncDepartment --cli-unfold-argument  \
    --Header.HospitalId 001 \
    --Header.Token tai.4d563878587a67774d44417a4e544d344e413d3d.1959c3405c614d709babfad5e1b79d54 \
    --Data.Cmd 2 \
    --Data.List.0.Id 123 \
    --Data.List.0.Name 综合门诊 \
    --Data.List.0.Scope 2 \
    --Data.List.0.OutpatientOn True \
    --Data.List.0.InHospitalOn True
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "List": []
        },
        "Message": "success",
        "RequestId": "a2c89afa-1b0d-40dc-87f3-acd0583c21bf"
    }
}
```

