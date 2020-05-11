class vpn:

    def vpn_list(self, project_id):

        vpn_exist = False

        from gcp_project_deletion.variable import service

        vpn_list_request = service.networks().list(project = project_id)

        vpn_list_response = vpn_list_request.execute()

        vpn_details = vpn_list_response.get("items", "")

        len(vpn_details)

        if len(vpn_details) > 0:

            vpn_exist = True

            print("VPN exists in project, please delete")

        else:

            print("VPN does not exists in the project ")

        return vpn_exist