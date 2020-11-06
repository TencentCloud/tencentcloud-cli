**Example 1: Creating public network-based migration task for RDS**

This example shows you how to migrate an RDS 5.6 instance fully and incrementally over the public network.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                                    // DTS task name' \
    --SrcDatabaseType 'mysql                           	 // Source instance type: MySQL' \
    --SrcAccessType 'extranet                              // Migration over the public network' \
    --DstDatabaseType 'mysql                               // Target instance type: MySQL' \
    --DstAccessType 'cdb                                   // Target instance type: TencentDB for MySQL' \
    --MigrateOption.RunMode '1                  			 // Immediate execution' \
    --MigrateOption.MigrateType '3                 		 // Full + incremental migration' \
    --MigrateOption.MigrateObject '1              		 // Entire instance' \
    --MigrateOption.ConsistencyType '5          			 // No check' \
    --SrcInfo.AccessKey 'cdb-powiqx8q            			 // Alibaba Cloud AccessKey' \
    --SrcInfo.RdsInstanceId 'rm-uf546i98x6ngqjnjx		 	 // Alibaba Cloud RDS instance ID' \
    --SrcInfo.Ip 106.13.216.14 \
    --SrcInfo.Port 3306 \
    --SrcInfo.User 'root                                   // Source instance username' \
    --SrcInfo.Supplier 'aliyun                             // Alibaba Cloud instance migration' \
    --SrcInfo.Password '123456                          	 // Source instance password' \
    --SrcInfo.Region 'ap-guangzhou                  		 // Source instance region: Guangzhou' \
    --DstInfo.InstanceId 'cdb-d0dqi8nv             		 // Target instance ID' \
    --DstInfo.Region 'ap-shanghai                     	 // Target region: Shanghai'
```

Output: 
```
{
    "Response": {
        "JobId": "dts-p01oy6qp",
        "RequestId": "2fcd891c-32f4-bf82-a8c0-16c99d75e175"
    }
}
```

**Example 2: Creating Direct Connect-based data migration task**

This example shows you how to fully and incrementally migrate a Direct Connect-based MySQL instance in Guangzhou to the TencentDB for MySQL instance cdb-d0dqi8nv in Shanghai and spot check the data consistency.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                                    // DTS task name' \
    --SrcDatabaseType 'mysql                          	 // Source instance type: MySQL' \
    --SrcAccessType 'dcg                                   // Migration over the public network' \
    --DstDatabaseType 'mysql                 		         // Target instance type: MySQL' \
    --DstAccessType 'cdb                                   // Target instance type: TencentDB for MySQL' \
    --MigrateOption.RunMode '1              		         // Immediate execution' \
    --MigrateOption.MigrateType '3                 		 // Full + incremental migration' \
    --MigrateOption.MigrateObject '1         			     // Entire instance migration' \
    --MigrateOption.ConsistencyType '3       				 // Spot check' \
    --MigrateOption.ConsistencyParams.SelectRowsPerTable '10    // Randomly select 20% of tables and 10% of entries in each table for data content verification' \
    --MigrateOption.ConsistencyParams.TablesSelectAll 20 \
    --MigrateOption.ConsistencyParams.TablesSelectCount '30     // Randomly select 30% of tables for record entry verification, i.e., `Select count(*)`' \
    --MigrateOption.IsOverrideRoot '0             // Do not overwrite the target database with source database root account' \
    --SrcInfo.UniqDcgId 'dcg-cyrjcc09              		// Direct Connect gateway ID' \
    --SrcInfo.VpcId 'vpc-72jblfaa                       	// VPC ID' \
    --SrcInfo.SubnetId 'subnet-7raec42a           		// Subnet ID' \
    --SrcInfo.Ip '192.168.120.136                         // Source instance IP' \
    --SrcInfo.Port '3307                                  // Source instance port' \
    --SrcInfo.User 'root                                  // Source instance username' \
    --SrcInfo.Supplier 'others                            // Non-Alibaba Cloud instance migration' \
    --SrcInfo.Password '123456                            // Source instance password' \
    --SrcInfo.Region 'ap-guangzhou                  		// Source instance region: Guangzhou' \
    --DstInfo.InstanceId 'cdb-d0dqi8nv       			    // Target instance ID' \
    --DstInfo.Region 'ap-shanghai                     		// Target region: Shanghai' \
    --DstInfo.ReadOnly '1                                 // The target instance is read-only'
```

Output: 
```
{
    "Response": {
        "JobId": "dts-o3s1vxsp",
        "RequestId": "915bc42a-714f-4faa-915b-a51cc09f5714"
    }
}
```

**Example 3: Creating TencentDB migration task**

This example shows you how to perform structural migration of selected tables from one TencentDB for MySQL instance to another instance without performing data consistency check.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                                    // DTS task name' \
    --SrcDatabaseType 'mysql                           	 // Source instance type: MySQL' \
    --SrcAccessType 'cdb                                   // TencentDB migration' \
    --DstDatabaseType 'mysql                               // Target instance type: MySQL' \
    --DstAccessType 'cdb                                   // Target instance type: TencentDB for MySQL' \
    --MigrateOption.RunMode '1                  			 // Immediate execution' \
    --MigrateOption.MigrateType '1                 		 // Structural migration' \
    --MigrateOption.MigrateObject '2              		 // Migration of specified tables' \
    --DatabaseInfo '[{"Database":"test","Table":["user","log"]}]    // Table to be migrated' \
    --MigrateOption.ConsistencyType '5          			 // No check' \
    --SrcInfo.InstanceId 'cdb-powiqx8q            		 // Source instance ID' \
    --SrcInfo.User 'root                                   // Source instance username' \
    --SrcInfo.Supplier 'others                             // Non-Alibaba Cloud instance migration' \
    --SrcInfo.Password '123456                          	 // Source instance password' \
    --SrcInfo.Region 'ap-guangzhou                  		 // Source instance region: Guangzhou' \
    --DstInfo.InstanceId 'cdb-d0dqi8nv             		 // Target instance ID' \
    --DstInfo.Region 'ap-shanghai                     	 // Target region: Shanghai'
```

Output: 
```
{
    "Response": {
        "JobId": "dts-46i7easd",
        "RequestId": "bc94c57b-9d69-11e9-84cb-256e968056b0"
    }
}
```

**Example 4: Creating public network-based data migration task**

This example shows you how to fully migrate the data from a public network MySQL instance in Guangzhou to the TencentDB for MySQL instance cdb-e78e0nnv in Shanghai and perform a full data consistency check.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                               // DTS task name' \
    --SrcDatabaseType 'mysql                          // Source instance type: MySQL' \
    --SrcAccessType 'extranet                         // Migration over the public network' \
    --DstDatabaseType 'mysql                          // Target instance type: MySQL' \
    --DstAccessType 'cdb                                   // Target instance access type: TencentDB for MySQL' \
    --MigrateOption.RunMode '1                        // Immediate execution' \
    --MigrateOption.MigrateType '2  	                // Full' \
    --MigrateOption.MigrateObject '1  	            // Entire instance migration' \
    --MigrateOption.ConsistencyType '2    		    // Full data consistency check' \
    --MigrateOption.IsOverrideRoot '0            // Do not overwrite the target database with source database root account' \
    --SrcInfo.Ip '14.17.22.36                         // Public IP of source instance' \
    --SrcInfo.Port '10301                             // Public port of source instance' \
    --SrcInfo.User 'root                              // Source instance username' \
    --SrcInfo.Supplier 'others                        // Non-Alibaba Cloud instance migration' \
    --SrcInfo.Password '123456                        // Source instance password' \
    --SrcInfo.Region 'ap-guangzhou             	    // Source instance region: Guangzhou' \
    --DstInfo.InstanceId 'cdb-e78e0nnv            	// Target instance ID' \
    --DstInfo.Region 'ap-shanghai                     // Target region: Shanghai' \
    --DstInfo.ReadOnly '1                             // The target instance is read-only'
```

Output: 
```
{
    "Response": {
        "JobId": "dts-1kl0iy0v",
        "RequestId": "2201c42a-714f-4faa-915b-a51cc09f5cec"
    }
}
```

