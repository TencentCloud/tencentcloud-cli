**Example 1: OpenMySql**



Input: 

```
tccli tcb CreateMySQL --cli-unfold-argument  \
    --EnvId **s*e*******g1**dbc0df14561 \
    --DbInstanceType MYSQL \
    --MysqlVersion 5.7 \
    --VpcId vpc-py****** \
    --SubnetId subnet-68r***** \
    --LowerCaseTableNames 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "38661"
        },
        "RequestId": "04b9fb5b-97c6-4b87-b926-e7d49c99c974"
    }
}
```

