class main:

    def services_exist(self):

        projects = os.getenv("Project_id")

        projects_list = projects.split(",")

        for projects in projects_list:

            project_id = projects

            print("Checking for VM's, Disks, VPN and Firewalls in project " + project_id)

            from gcp_project_deletion_services.compute import compute

            obj_compute = compute()

            instance_exist = obj_compute.vm_list(project_id)

            from gcp_project_deletion_services.disks import disks

            obj_disk = disks()

            disks_exist = obj_disk.disks_list(project_id)

            from gcp_project_deletion.firewall import firewall

            obj_firewall = firewall()

            firewall_exist = obj_firewall.firewall_list(project_id)

            from gcp_project_deletion.vpn import vpn

            obj_vpn = vpn()

            vpn_exist = obj_vpn.vpn_list(project_id)

            from gcp_project_deletion.storage import storage

            obj_storage = storage()

            storage_exist = obj_storage.storage_list(project_id)

            from gcp_project_deletion.liens import liens

            obj_liens = liens()

            liens_exist = obj_liens.liens_list(project_id)

            from gcp_project_deletion.endpoint import endpoint

            obj_endpoint = endpoint()

            endpoint_exist = obj_endpoint.endpoint_list(project_id)

            if (instance_exist | disks_exist | firewall_exist | vpn_exist | liens_exist | endpoint_exist):

                print("vm exists in Project "+project_id+" and it will not  be deleted")

            else:

                from gcp_project_deletion.variable import resource_manager_service

                request = resource_manager_service.projects().delete(projectId=project_id)

                request.execute()

                print("Project "+project_id+" is now shutdown")

obj_main = main()

obj_main.services_exist()