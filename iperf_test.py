import testparser

class TestSuite:
    def test_iperf3_client_connection(self, client):
        result, errors = client
        assert not errors, f"iperf test errors: {errors}"
        network_info = testparser.parse_output(result)
        print(network_info)
        for transfer in network_info['Transfer']:
            assert float(transfer) > 2
         
        for bandwidth in network_info['Bandwidth']:
            assert float(bandwidth) > 20
