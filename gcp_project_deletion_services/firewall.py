class firewall:

    def firewall_list(self, project_id):

        from gcp_project_deletion_services.variable import service

        firewall_request = service.firewalls().list(project=project_id)

        firewall_response = firewall_request.execute()

        firewall_details = firewall_response.get("items", "")

        firewall_name_list = [sub['name'] for sub in firewall_details]

        if len(firewall_name_list)>0:

            for firewall_name in firewall_name_list:

                firewall_delete_request = service.firewalls().delete(project=project_id, firewall=firewall_name)

                firewall_delete_response = firewall_delete_request.execute()

        firewall_exist = False

        return firewall_exist



