from utils import TestCli

def test_describe_regions():
    cmd = 'tccli cvm DescribeRegions'
    expect = "\"Region\": \"ap-guangzhou\""
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_describe_instances():
    cmd = 'tccli cvm DescribeInstances'
    expect = "\"TotalCount\":"
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_describe_disaster_disaster_recover_group_quota():
    cmd = 'tccli cvm DescribeDisasterRecoverGroupQuota'
    expect = "\"CvmInHostGroupQuota\":"
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_describe_disaster_recover_groups():
    cmd = 'tccli cvm DescribeDisasterRecoverGroups'
    expect = "DisasterRecoverGroupSet"
    test_cli = TestCli()
    test_cli.equal(cmd, expect)


def test_describe_hosts():
    cmd = 'tccli cvm DescribeHosts --cli-unfold-argument'
    cmd += ' --Filters.0.Name zone'
    cmd += ' --Filters.0.Values ap-guangzhou-2'
    cmd += ' --Offset 0 --Limit 20'
    expect = "\"HostSet\": []"
    test_cli = TestCli()
    test_cli.equal(cmd, expect)
