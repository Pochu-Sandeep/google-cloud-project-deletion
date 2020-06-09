class vpn:

    def vpn_list(self, project_id):

        from gcp_project_deletion_services.variable import service

        vpn_list_request = service.networks().list(project = project_id)

        vpn_list_response = vpn_list_request.execute()

        vpn_details = vpn_list_response.get("items", "")

        if len(vpn_details)>0:

            #vpn_exist = True

            vpn_name_list = [sub['name'] for sub in vpn_details]

            for vpn_name in vpn_name_list:

                request = service.networks().delete(project=project_id, network=vpn_name)

                response = request.execute()

        else:
            
            print("VPN deleted")

            vpn_exist = False

        return vpn_exist

