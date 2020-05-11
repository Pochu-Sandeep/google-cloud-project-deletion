class liens:

    def liens_list(self,project_id):

        liens_exist = False

        from gcp_project_deletion.variable import resource_manager_service

        request = resource_manager_service.liens().list(parent="projects/"+project_id)

        response = request.execute()

        for lien in response.get('liens',[]):

            lien_name = lien.get("name")

            if len(lien_name) > 0:

                liens_exist = True

                break

        if liens_exist:

            print("Liens exists in project please delete ")

        else:

            print("Liens doesn't exists in the project")

        return liens_exist


