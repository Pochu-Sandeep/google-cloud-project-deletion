class liens:

    def liens_list(self,project_id):

        from gcp_project_deletion_services.variable import resource_manager_service

        request = resource_manager_service.liens().list(parent="projects/"+project_id)

        response = request.execute()

        for lien in response.get('liens',[]):

            lien_name = lien.get("name")

            print(lien_name)

            if len(lien_name)>0:

                request = resource_manager_service.liens().delete(name=lien_name)

                request.execute()

        liens_exist = False

        return liens_exist



