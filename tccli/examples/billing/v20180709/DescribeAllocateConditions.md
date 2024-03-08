**Example 1: 查询分账条件**

查询分账条件

Input: 

```
tccli billing DescribeAllocateConditions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Business": [
            {
                "Children": [
                    {},
                    {}
                ]
            },
            {
                "Children": [
                    {}
                ]
            },
            {
                "Children": [
                    {}
                ]
            },
            {
                "Children": [
                    {}
                ]
            },
            {
                "Children": [
                    {}
                ]
            },
            {
                "Children": [
                    {},
                    {}
                ]
            },
            {
                "Children": [
                    {}
                ]
            }
        ],
        "OwnerUin": [
            {
                "OwnerUin": "700000384179"
            }
        ],
        "OperateUin": [
            {
                "OperateUin": "700000384179"
            }
        ],
        "Product": [
            {
                "ProductCode": "sp_cvm_s1",
                "ProductCodeName": "云服务器CVM-标准型S1"
            },
            {
                "ProductCode": "sp_cbs_premium",
                "ProductCodeName": "高性能云硬盘"
            },
            {
                "ProductCode": "sp_cos_pkg_std_new",
                "ProductCodeName": "COS 标准存储容量包 new"
            },
            {
                "ProductCode": "sp_cvm_s2",
                "ProductCodeName": "云服务器CVM-标准型S2"
            },
            {
                "ProductCode": "sp_rav_audio_video",
                "ProductCodeName": "实时音视频-音视频通话"
            },
            {
                "ProductCode": "sp_cdn_cn_flux_package",
                "ProductCodeName": "中国境内CDN流量包"
            },
            {
                "ProductCode": "sp_ci_pkg_im_com",
                "ProductCodeName": "CI 图片压缩资源包"
            },
            {
                "ProductCode": "sp_redis_single",
                "ProductCodeName": "云数据库Redis-社区版"
            },
            {
                "ProductCode": "sp_ci_pkg_co_re",
                "ProductCodeName": "万象-COS-内容识别资源包"
            }
        ],
        "ActionType": [
            {
                "ActionType": "prepay_purchase",
                "ActionTypeName": "包年包月新购"
            },
            {
                "ActionType": "prepay_return",
                "ActionTypeName": "包年包月退款"
            },
            {
                "ActionType": "prepay_modify",
                "ActionTypeName": "包年包月配置变更"
            },
            {
                "ActionType": "prepay_renew",
                "ActionTypeName": "包年包月续费"
            }
        ],
        "Item": [
            {
                "ItemCode": "sv_cvm_bandwidth_prepay",
                "ItemCodeName": "带宽-按带宽计费"
            },
            {
                "ItemCode": "sv_cbs_memspace_premium",
                "ItemCodeName": "高性能云硬盘-存储空间"
            },
            {
                "ItemCode": "sv_cos_pkg_std_new_20",
                "ItemCodeName": "COS 标准存储容量包 20GB new"
            },
            {
                "ItemCode": "virtual_v_cvm_compute_s2",
                "ItemCodeName": "计算组件"
            },
            {
                "ItemCode": "sv_cvm_rootdisk_cbspremium",
                "ItemCodeName": "高效云系统盘"
            },
            {
                "ItemCode": "sv_rav_audio_video_custom_free",
                "ItemCodeName": "音视频通话-赠送套餐包"
            },
            {
                "ItemCode": "sv_cvm_rootdisk_local",
                "ItemCodeName": "本地系统盘"
            },
            {
                "ItemCode": "virtual_v_cvm_compute_s1",
                "ItemCodeName": "计算组件"
            },
            {
                "ItemCode": "sv_cdn_cn_flux_package",
                "ItemCodeName": "CDN流量包-流量"
            },
            {
                "ItemCode": "sv_ci_pkg_im_com_10",
                "ItemCodeName": "CI 图片压缩资源包 10万次"
            },
            {
                "ItemCode": "sv_redis_mem_single",
                "ItemCodeName": "云数据库Redis-社区版-内存"
            },
            {
                "ItemCode": "sv_ci_pkg_co_re_10",
                "ItemCodeName": "万象-COS-内容识别资源包 10万次"
            },
            {
                "ItemCode": "sv_rav_audio_video_assign_formal",
                "ItemCodeName": "实时音视频-音视频通话-固定套餐包"
            },
            {
                "ItemCode": "sv_cos_pkg_std_new_10",
                "ItemCodeName": "COS 标准存储容量包 10GB new"
            }
        ],
        "InstanceType": [
            {
                "InstanceType": "ri",
                "InstanceTypeName": "预留实例"
            },
            {
                "InstanceType": "svp",
                "InstanceTypeName": "节省计划"
            },
            {
                "InstanceType": "si",
                "InstanceTypeName": "竞价实例"
            },
            {
                "InstanceType": "rp",
                "InstanceTypeName": "资源包"
            },
            {
                "InstanceType": "capacityReserve",
                "InstanceTypeName": "容量预留"
            }
        ],
        "Region": [
            {
                "RegionId": 0,
                "RegionName": "其他"
            },
            {
                "RegionId": 1,
                "RegionName": "华南地区（广州）"
            },
            {
                "RegionId": 3,
                "RegionName": "华北地区（北京(北京一区 原天津)）"
            },
            {
                "RegionId": 4,
                "RegionName": "华东地区（上海）"
            },
            {
                "RegionId": 5,
                "RegionName": "港澳台地区（香港）"
            },
            {
                "RegionId": 6,
                "RegionName": "北美地区（多伦多）"
            },
            {
                "RegionId": 7,
                "RegionName": "华东地区（上海金融）"
            },
            {
                "RegionId": 8,
                "RegionName": "华北地区（北京）"
            },
            {
                "RegionId": 9,
                "RegionName": "东南亚地区（新加坡）"
            },
            {
                "RegionId": 11,
                "RegionName": "华南地区（深圳金融）"
            },
            {
                "RegionId": 12,
                "RegionName": "华南地区（广州OPEN）"
            },
            {
                "RegionId": 15,
                "RegionName": "美西地区（美国硅谷）"
            },
            {
                "RegionId": 16,
                "RegionName": "西南地区（成都）"
            },
            {
                "RegionId": 17,
                "RegionName": "欧洲地区（法兰克福）"
            },
            {
                "RegionId": 18,
                "RegionName": "亚太地区（首尔）"
            },
            {
                "RegionId": 19,
                "RegionName": "西南地区（重庆）"
            },
            {
                "RegionId": 21,
                "RegionName": "亚太地区（印度）"
            },
            {
                "RegionId": 22,
                "RegionName": "美东地区（弗吉尼亚）"
            },
            {
                "RegionId": 23,
                "RegionName": "亚太地区（泰国）"
            },
            {
                "RegionId": 24,
                "RegionName": "欧洲地区（欧洲东北）"
            },
            {
                "RegionId": 25,
                "RegionName": "亚太地区（日本）"
            },
            {
                "RegionId": 31,
                "RegionName": "华东地区（济南）"
            },
            {
                "RegionId": 32,
                "RegionName": "华东地区（杭州）"
            },
            {
                "RegionId": 33,
                "RegionName": "华东地区（南京）"
            },
            {
                "RegionId": 34,
                "RegionName": "华东地区（福州）"
            },
            {
                "RegionId": 35,
                "RegionName": "华中地区（武汉）"
            },
            {
                "RegionId": 36,
                "RegionName": "华北地区（天津）"
            },
            {
                "RegionId": 37,
                "RegionName": "华南地区（深圳）"
            },
            {
                "RegionId": 39,
                "RegionName": "港澳台地区（台北）"
            },
            {
                "RegionId": 41,
                "RegionName": "中东地区（迪拜）"
            },
            {
                "RegionId": 42,
                "RegionName": "美国南部（洛杉矶）"
            },
            {
                "RegionId": 43,
                "RegionName": "南美地区（巴西圣保罗互联区）"
            },
            {
                "RegionId": 44,
                "RegionName": "澳洲地区（悉尼）"
            },
            {
                "RegionId": 45,
                "RegionName": "华中地区（长沙）"
            },
            {
                "RegionId": 46,
                "RegionName": "华北地区（北京金融）"
            },
            {
                "RegionId": 47,
                "RegionName": "其他地区（其他）"
            },
            {
                "RegionId": 53,
                "RegionName": "华北地区（石家庄）"
            },
            {
                "RegionId": 54,
                "RegionName": "华南地区（清远）"
            },
            {
                "RegionId": 55,
                "RegionName": "华东地区（合肥）"
            },
            {
                "RegionId": 56,
                "RegionName": "东北地区（沈阳）"
            },
            {
                "RegionId": 57,
                "RegionName": "西北地区（西安）"
            },
            {
                "RegionId": 58,
                "RegionName": "西北地区（西北）"
            },
            {
                "RegionId": 71,
                "RegionName": "华中地区（郑州）"
            },
            {
                "RegionId": 72,
                "RegionName": "亚太东南地区（雅加达）"
            },
            {
                "RegionId": 73,
                "RegionName": "华南地区（清远信安）"
            },
            {
                "RegionId": 74,
                "RegionName": "南美地区（圣保罗）"
            },
            {
                "RegionId": 76,
                "RegionName": "西南地区（贵阳）"
            },
            {
                "RegionId": 77,
                "RegionName": "华南地区（深圳深宇财付通）"
            },
            {
                "RegionId": 78,
                "RegionName": "华东地区（上海自动驾驶云）"
            },
            {
                "RegionId": 79,
                "RegionName": "华南地区（深圳金融专区(TCE)）"
            },
            {
                "RegionId": 81,
                "RegionName": "华东地区（上海金融专区(TCE)）"
            },
            {
                "RegionId": 1001,
                "RegionName": "亚太地区（亚太一区）"
            },
            {
                "RegionId": 1002,
                "RegionName": "亚太地区（亚太二区）"
            },
            {
                "RegionId": 1003,
                "RegionName": "亚太地区（亚太三区）"
            },
            {
                "RegionId": 1004,
                "RegionName": "中东地区（中东）"
            },
            {
                "RegionId": 1005,
                "RegionName": "欧洲地区（欧洲）"
            },
            {
                "RegionId": 1006,
                "RegionName": "北美地区（北美）"
            },
            {
                "RegionId": 1007,
                "RegionName": "南美地区（南美）"
            },
            {
                "RegionId": 1008,
                "RegionName": "非洲地区（非洲）"
            },
            {
                "RegionId": 1009,
                "RegionName": "中国大陆（中国大陆）"
            },
            {
                "RegionId": 1010,
                "RegionName": "自定义区（自定义区）"
            },
            {
                "RegionId": 2009,
                "RegionName": "境内地区（中国大陆通用）"
            },
            {
                "RegionId": 2010,
                "RegionName": "境外地区（中国港澳台与海外通用）"
            }
        ],
        "PayMode": [
            {
                "PayMode": "prePay",
                "PayModeName": "包年包月"
            },
            {
                "PayMode": "postPay",
                "PayModeName": "按量计费"
            },
            {
                "PayMode": "riPay",
                "PayModeName": "预留实例"
            }
        ],
        "Project": [
            {
                "ProjectId": 0,
                "ProjectName": "默认项目"
            }
        ],
        "Tag": [
            {
                "TagKey": "yzd_key2",
                "TagValue": "yzd_value2"
            },
            {
                "TagKey": "key1",
                "TagValue": "value1"
            },
            {
                "TagKey": "key2",
                "TagValue": "value2"
            },
            {
                "TagKey": "key3",
                "TagValue": "value3"
            },
            {
                "TagKey": "yzd_key1",
                "TagValue": "yzd_value2"
            }
        ],
        "RequestId": "da214fee-dcee-4b23-96b7-8dcd6cab1345"
    }
}
```

