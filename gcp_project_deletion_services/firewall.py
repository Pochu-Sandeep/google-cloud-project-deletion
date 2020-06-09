class firewall:

    def firewall_list(self, project_id):

        from gcp_project_deletion.variable import service

        firewall_request = service.firewalls().list(project=project_id)

        firewall_response = firewall_request.execute()

        print(len(firewall_response))

        for firewall_details in firewall_response.get("items", ""):

            print(len(firewall_details))

            firewall_name = firewall_details.get("name")

            if len(firewall_name)>0:

                firewall_exist = True

                firewall_delete_request = service.firewalls().delete(project=project_id, firewall=firewall_name)

                firewall_delete_response = firewall_delete_request.execute()

            else:

                firewall_exist = False

        return firewall_exist

