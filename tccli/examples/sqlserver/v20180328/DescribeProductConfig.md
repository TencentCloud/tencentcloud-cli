**Example 1: Querying purchasable specification information in a specified AZ of a specified region**



Input: 

```
tccli sqlserver DescribeProductConfig --cli-unfold-argument  \
    --Zone ap-guangzhou-2
```

Output: 
```
{
	"Response": {
		"RequestId": "2b384401-0537-4e81-b78d-473c80ee6f7a",
		"SpecInfoList": [
				"CPU": 2,
				"MachineType": "TS85",
				"MachineTypeName": "High-IO",
				"MaxStorage": 3000,
				"Memory": 16000000,
				"MinStorage": 10,
				"Pid": 10908,
				"QPS": 16800,
				"SpecId": 18,
				"SuitInfo": "Small-scale apps with tens of thousands of UVs",
				"Version": "2008R2",
				"VersionName": "SQL Server 2008 Enterprise"
			},
			{
				"CPU": 2,
				"MachineType": "TS85",
				"MachineTypeName": "High-IO",
				"MaxStorage": 3000,
				"Memory": 16000000,
				"MinStorage": 10,
				"Pid": 10908,
				"QPS": 16800,
				"SpecId": 18,
				"SuitInfo": "Small-scale apps with tens of thousands of UVs",
				"Version": "2012SP3",
				"VersionName": "SQL Server 2012 Enterprise"
			},
			{
				"CPU": 2,
				"MachineType": "TS85",
				"MachineTypeName": "High-IO",
				"MaxStorage": 3000,
				"Memory": 16000000,
				"MinStorage": 10,
				"Pid": 10908,
				"QPS": 16800,
				"SpecId": 18,
				"SuitInfo": "Small-scale apps with tens of thousands of UVs",
				"Version": "2016SP1",
				"VersionName": "SQL Server 2016 Enterprise"
			}
		],
		"TotalCount": 27
	}
}
```

