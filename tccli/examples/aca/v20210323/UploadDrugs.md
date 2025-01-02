**Example 1: 药品同步**



Input: 

```
tccli aca UploadDrugs --cli-unfold-argument  \
    --Header.HospitalId 1 \
    --Header.Token tai.MTAwMDY%3D.30100b80-42af-11eb-b203-19b451462f39 \
    --Data.Drugs.0.DrugOrgId 医院药品id \
    --Data.Drugs.0.DrugName 医院药品通用名 \
    --Data.Drugs.0.DrugCommodityName 医院药品商品名 \
    --Data.Drugs.0.Specifications 医院药品规格 \
    --Data.Drugs.0.ApprovalNumber 医院药品批准文号 \
    --Data.Drugs.0.Manufacturer 医院厂商 \
    --Data.Drugs.0.DosageForm 剂型 \
    --Data.Drugs.0.DosageFormCode 剂型编码 \
    --Data.Drugs.0.DefinedDailyDose 抗菌药DDD值 \
    --Data.Drugs.0.Amount 药品单价 \
    --Data.Drugs.0.YbCode 国家医保编码 \
    --Data.Drugs.0.DrugBasicCode 药品本位码 \
    --Data.Drugs.0.Unuse 0 \
    --Data.Drugs.0.PropertyInfo.DrugType 1 \
    --Data.Drugs.0.PropertyInfo.AntibacterialType 0 \
    --Data.Drugs.0.PropertyInfo.AntibacterialClass 0 \
    --Data.Drugs.0.PropertyInfo.SpeciallyDrugType 0 \
    --Data.Drugs.0.PropertyInfo.IsBasicDrug 1 \
    --Data.Drugs.0.PropertyInfo.ChargeType 2
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Message": "成功",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Data": {
            "Dummy": false
        }
    }
}
```

