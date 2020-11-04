**Example 1: 创建公网数据迁移任务**

将用户的mysql公网实例数据, 采用全量方式迁移到腾讯云上海地域的cdb-e78e0nnv实例上. 其中源实例的接入地域为广州. 数据一致性检查做全量检测.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                               // DTS任务名称'\
    --SrcDatabaseType 'mysql                          // 源实例是mysql'\
    --SrcAccessType 'extranet                         // 公网迁移'\
    --DstDatabaseType 'mysql                          // 目标实例mysql'\
    --DstAccessType 'cdb                              // 目标实例是腾讯云mysql'\
    --MigrateOption.RunMode '1                        // 立即执行'\
    --MigrateOption.MigrateType '2  	                // 全量'\
    --MigrateOption.MigrateObject '1  	            // 整实例迁移'\
    --MigrateOption.ConsistencyType '2    		    // 做全量数据一致性检测'\
    --MigrateOption.IsOverrideRoot '0            		// 不覆盖目标库root'\
    --SrcInfo.Ip '14.17.22.36                         // 源实例公网IP'\
    --SrcInfo.Port '10301                             // 源实例公网Port'\
    --SrcInfo.User 'root                              // 源实例用户名'\
    --SrcInfo.Supplier 'others                        // 非阿里迁移'\
    --SrcInfo.Password '123456                        // 源实例密码'\
    --SrcInfo.Region 'ap-guangzhou             	    // 源实例地域广州'\
    --DstInfo.InstanceId 'cdb-e78e0nnv            	//  目标实例ID'\
    --DstInfo.Region 'ap-shanghai                     // 目标地域上海'\
    --DstInfo.ReadOnly '1                             // 目标实例只读'
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

**Example 2: 创建专线数据迁移任务**

将用户通过专线接入的mysql实例,  全量+增量迁移迁移到腾讯云上海地域的cdb-d0dqi8nv实例上. 其中源实例的接入地域为广州. 做数据一致性抽样检查.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                                    // DTS任务名称'\
    --SrcDatabaseType 'mysql                          	 // 源实例是mysql'\
    --SrcAccessType 'dcg                                   // 公网迁移'\
    --DstDatabaseType 'mysql                 		         // 目标实例mysql'\
    --DstAccessType 'cdb                                   // 目标实例是腾讯云mysql'\
    --MigrateOption.RunMode '1              		         // 立即执行'\
    --MigrateOption.MigrateType '3         		         // 全量+增量迁移'\
    --MigrateOption.MigrateObject '1         			     // 整实例迁移'\
    --MigrateOption.ConsistencyType '3       				 // 抽样检测'\
    --MigrateOption.ConsistencyParams.SelectRowsPerTable '10    // 随机抽取20% 的表，每张表随机抽取10%的记录进行数据内容校验'\
    --MigrateOption.ConsistencyParams.TablesSelectAll 20\
    --MigrateOption.ConsistencyParams.TablesSelectCount '30     // 随机抽取30% 的表进行记录条数校验，即Select count(*)'\
    --MigrateOption.IsOverrideRoot '0             		// 不覆盖目标库root'\
    --SrcInfo.UniqDcgId 'dcg-cyrjcc09              		// 专线网关ID'\
    --SrcInfo.VpcId 'vpc-72jblfaa                       	// 私有网络ID'\
    --SrcInfo.SubnetId 'subnet-7raec42a           		// 子网ID'\
    --SrcInfo.Ip '192.168.120.136                         // 源实例IP'\
    --SrcInfo.Port '3307                                  // 源实例Port'\
    --SrcInfo.User 'root                                  // 源实例用户名'\
    --SrcInfo.Supplier 'others                            // 非阿里迁移'\
    --SrcInfo.Password '123456                            // 源实例密码'\
    --SrcInfo.Region 'ap-guangzhou                  		// 源实例地域广州'\
    --DstInfo.InstanceId 'cdb-d0dqi8nv       			    // 目标实例ID'\
    --DstInfo.Region 'ap-shanghai                    		// 目标地域上海'\
    --DstInfo.ReadOnly '1                                 // 目标实例只读'
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

**Example 3: 创建云数据库迁移任务**

从腾讯云mysql实例结构迁移到腾讯云另一个mysql实例，选择部分库表做，不做数据一致性检查。

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                                    // DTS任务名称'\
    --SrcDatabaseType 'mysql                           	 // 源实例是mysql'\
    --SrcAccessType 'cdb                                   // 云数据库迁移'\
    --DstDatabaseType 'mysql                               // 目标实例mysql'\
    --DstAccessType 'cdb                                   // 目标实例是腾讯云mysql'\
    --MigrateOption.RunMode '1                  			 // 立即执行'\
    --MigrateOption.MigrateType '1                 		 // 结构迁移'\
    --MigrateOption.MigrateObject '2              		 // 指定库表迁移'\
    --DatabaseInfo '[{"Database":"test","Table":["user","log"]}]    // 需要迁移的库表'\
    --MigrateOption.ConsistencyType '5          			 // 不检测'\
    --SrcInfo.InstanceId 'cdb-powiqx8q            		 // 源实例ID'\
    --SrcInfo.User 'root                                   // 源实例用户名'\
    --SrcInfo.Supplier 'others                             // 非阿里迁移'\
    --SrcInfo.Password '123456                          	 // 源实例密码'\
    --SrcInfo.Region 'ap-guangzhou                  		 // 源实例地域广州'\
    --DstInfo.InstanceId 'cdb-d0dqi8nv             		 // 目标实例ID'\
    --DstInfo.Region 'ap-shanghai                     	 // 目标地域上海'
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

**Example 4: 创建RDS公网迁移任务**

通过公网，迁移RDS5.6实例，全量+增量迁移。

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 'usertest                                    // DTS任务名称'\
    --SrcDatabaseType 'mysql                           	 // 源实例是mysql'\
    --SrcAccessType 'extranet                              // 公网迁移'\
    --DstDatabaseType 'mysql                               // 目标实例mysql'\
    --DstAccessType 'cdb                                   // 目标实例是腾讯云mysql'\
    --MigrateOption.RunMode '1                  			 // 立即执行'\
    --MigrateOption.MigrateType '3                 		 // 全量+增量迁移'\
    --MigrateOption.MigrateObject '1              		 // 整个实例'\
    --MigrateOption.ConsistencyType '5          			 // 不检测'\
    --SrcInfo.AccessKey 'cdb-powiqx8q            			 // 阿里云AccessKey'\
    --SrcInfo.RdsInstanceId 'rm-uf546i98x6ngqjnjx		 	 // 阿里云RDS实例ID'\
    --SrcInfo.Ip 106.13.216.14\
    --SrcInfo.Port 3306\
    --SrcInfo.User 'root                                   // 源实例用户名'\
    --SrcInfo.Supplier 'aliyun                             // 阿里迁移'\
    --SrcInfo.Password '123456                          	 // 源实例密码'\
    --SrcInfo.Region 'ap-guangzhou                  		 // 源实例地域广州'\
    --DstInfo.InstanceId 'cdb-d0dqi8nv             		 // 目标实例ID'\
    --DstInfo.Region 'ap-shanghai                     	 // 目标地域上海'
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

