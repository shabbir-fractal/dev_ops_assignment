## Assignment for "Basics of DevOps" Assignment

### Github Repo Link
https://github.com/shabbir-fractal/dev_ops_assignment

### Docker Hub Image Link
https://hub.docker.com/repositories/shabbirhussainbohra/devops_assignment_repo

### Steps involved in completing this assignment

1. Download Ecommerce shipping data csv from following link: https://www.kaggle.com/datasets/prachi13/customer-analytics?resource=download

2. Add following files in the project:
  - main.py
  - model.py
  - ecommerce_shipment_data.csv
  - requirement.txt

3. Create virtual env, activate it and install dependencies

4. Uncomment line no. 38 ``prepare_model()``  in model.py and run this file to generate model.pkl, comment the same line again once .pkl file is generated.

5. Test application locally by running fast api server

6. Check application in browser on http://localhost:8001/docs

7. Add following line for unit testing
  - run_server.sh
  - test_api.sh
  - test_main.py

8. execute unit test locally by running ``pytest`` in terminal

9. Add .gitignore 

10. initialize git repository by running ``git init``

11. Create new repository on Github account

12. Add repository origin. Stage, Commit and push all changes to newly created repository

13. Check your github account in browser and verify changes

14. Copy code to linux machine and add Dockerfile

15. Build docker image with tag

16. Run docker image in deattach mode and expose port (with -d and -p options)

17. Verify app in browser

18. Cleanup container

19. Create docker hub account if not exist then create access key

20. Create new repo in dockerhub

21. Add following Gihub screcrets
  - DOCKERHUB_USERNAME
  - DOCKERHUB_TOKEN

22. Create .github/workflow folder in app root and add ci.yml and cd.yml files

23. Commit github action changes and push to repo

24. Verify CI action by opening Github repo/actions i.e. https://github.com/shabbir-fractal/dev_ops_assignment/actions

25. Verify CD action 

26. Open docker hub account in browser and check image is pushed there

__Note__: Screenshots for each step can be found inside screenshots folder 