# README
---
# Hot Sauce Recipe Database

Written in reference to QAC - Fundamental Project Specification (DevOps Core) - revised edition. This project is for the purpose of fulfilling the specification definition for the project assignment due Week 5 of the DevOps February 17 2020 intake cohort.

## Table of Contents

1. [Project Brief](#project-brief)
    + [Proposal](#proposal)
2. [Trello Board](#trello-board)
    + [Start Point](#start-board)
    + [Rolling Changes](#rolling-changes)
    + [End Point](#end-point)
3. [Risk Assessment](#risk-assessment)
4. [Project Architecture](#project-architecture)
    + [Entity Relationship Diagram](#entity-relationship-diagram)
    + [Architecture Diagram](#architecture-diagram)
    + [Issues Encountered](#issues-encountered)
5. [Design Considerations](#design-considerations)
    + [Front End](#front-end)
    + [Back End](#back-end)
    + [UI](#ui)
6. [Testing](#testing)
    + [Pytest Testing](#pytest)
    + [Selenium Testing](#selenium)
    + [Final Report](#final-report)
7. [Deployment](#deployment)
    + [Toolset](#toolset)
    + [CI Server Implementation](#ci-server-implementation)
    + [Branch and Merge Log](#branch-and-merge-log)
8. [Front End Considerations](#front-end-considerations)
9. [Improvements for Future Versions](#improvements-for-future-versions)
+ [Authors](#authors)
+ [Acknowledgements](#acknowledgements)

## Project Brief

The project requires a CRUD functional website, based around a database with at least two tables joined by a joining table, with backend written in Python, fully version controlled, tested, and deployed via a Jenkins CI server.

### Proposal

My proposal focuses on the creation of a website for the sharing of hot sauce recipes. Recipes and ingredients can be added, and both can be joined on a joining table exhibiting a many to many relationship. The project will be autobuilt using a Jenkins pipeline with webhooks.

## Trello Board

I used a kanban board on Trello to manage my workflow during the project, the board was set to public to enable overview and broadcast. Agile methodology was implemented in line with the brief, in terms of product and sprint backlog, although due to the individual nature of the project, no scrum working practices were implemented. The board was set up with reference to potential user stories emphasising the CRUD functionality of the database system. Although unrequired, a Task Backlog was instituted in order to keep the requirements of the project spec clear, so as to enable sprint tasks to be dynamically allocated to them.

Due to this setup sprints could be passed through development, and, if required, testing, before being assigned to Done. Once sprints generated by a backlogged Task have been completed, the task itself can be marked Done. Errors, mistakes, and software bugs are given over to the newly added Bugs column, to be fed back to development and testing when identified and processed.

### Start Point

![A picture of the trello board, started on the first week. The Product Backlog, The Sprint Backlog, the Tasks for the first week have been added. Only the 'Start the Trello board' task has been completed](https://i.imgur.com/op4ChN4.png)

At the start of the project, I focussed on the four tasks most easily completable in the first week of training: Starting the Kanban board [itself](https://trello.com/b/8xaM1s0K/qa-week-5-individual-project-hotsaucerecipe), starting this documentation to streamline my future workflow, instituting a github repository for the project, which can be found [here](https://github.com/THC-QA/QA_SFIA_Project), and initialising the risk assessment for the project in line with my initial understanding.

### Rolling Changes

+ The first major change to the Kanban board was a respec to denote the removing of Selenium testing from the project, due to the lack of javascript implementation. In replacement, a provisional addition of Postman testing was added, so as to validate the REST API, and therefore CRUD functionality of our APIs. In addition, issues with reimaging hardware lead to the need to implement Visual Code Studio usage. To this end I installed the Remote SSH, mySQL, Python, and Code Spellchecker extensions, so as to improve project flow. Notepad++ is being explored in replacement of VIM for GitBASH. The database has been implemented as a simple relationship between two main tables, the user table has been omitted until hashing of passwords and pre-encryption can be handled on the app side.

+ An ERD was started on LucidChart, and a mockup of the database instituted on a GCP MySQL server. Should be noted due to the particular relationship between recipes and ingredients that it would be more efficient to use a noSQL database, albeit outside the project scope. The risk assessment was started, and will be added to as the project continues. Whilst this entire system could be run in the GitHub projects utility, this is again outside the scope of the brief. A GCP Compute instance is running Ubuntu is being used for the pythonic programming, and has been updated with the relevant modules, including Flask. Visual Studio Code is used for access.

+ The ERD was edited into its final version, and will be coloured appropriately to reflect the state of project at completion. A mySQL file has been created in order to institute the framework of the database to fulfil the MVP of the project brief. A further mySQL file acts as a secondary backup to populate the tables with example data to showcase the website.

+ A barebones CRUD functional website has been created in python, HTML, and CSS. It uses the Flask module with Jinja2, mysqlDB, and WTForms. Issues have been encountered involving WTForms implementation. Several of the user stories have been completed, but the others are on hold until the usefulness of a user system is decided on. A Requirements file has been added to the Flask app, currently hosted on a different repository pending Jenkins integration.

+ Website updated to full compliance with brief. User stories revised to reflect updated understanding of technical complexities. Favicon added as joke branding. Jenkinsfile added, and installation and pre-installation processing started. Problems involving exported environmental variables.

+ Jenkins pipeline updated to include URL testing phase. ChilliApp now runs as a service, GUnicorn integration problematic, but can replace debug mode on deployment. In contravention of usual working practice, Jenkins server exposed to web traffic in place of a reverse proxy, as ngrok or nginx integration is an issue.

+ Having looked hard at the feasibility of utilising Postman as an ancilliary service to the project, I elected to use Selenium after all. The time requirements for learning to use the program and creating a mockup could be better spent learning to use HTML id tags properly.

### End Point

## Risk Assessment


|Risk No.|Risk|Description|Hazard|Likelihood|Impact|Solution|
|---|---|---|---|---|---|---|
|1.0.1|Overrun on time.|Due to poor time management, the project is not completed.|Worst case scenario, marks are lost due to lack of coverage of brief.|2|5|Make good use of Kanban to manage workflow, and efficient time use of office resources.|
|1.0.2|Data breach on workstation.|Due to accident or malicious action, workstation is compromised.|Worst case scenario, severe progress loss.|1|5|Change passwords on workstation, keep e-services logged off when not in use.|
|1.1.1|Overrunning on GCP free data limits.|An instance is left running, or an account breach enables the resources on the account to be drained.|Worst case scenario, databases are unaccessable.|1|5|Continue monitoring GCP usage. Copy databases offline as final backup.|
|1.1.2.1|Database security: SQL|The GCP server is breached in some way, compromising data integrity.|Worst case scenario, data is lost, or user data is compromised.|3|5|Ensure user and personal data is encrypted, and passwords hashed, before being moved to the database.|
|1.1.2.2|Database security: SSH|Unmanaged connections cause data leak or damage, keys are lost or stolen.| Worst case scenario, GDPR noncompliance or total data compromisation.|2|5|Learn and make use of GCP's SSH key management role system, and implement it correctly.|
|1.1.2.3|Database security: SQL-I|Unsanitised user input allows SQL injection into the database.|Worst case scenario, database is maliciously destroyed.|2|5|Ensure any user accessible inputs are sanitised, and implement permission roles.|
|1.2.1|Flask password storage|Although Flask uses passwords fields, hashing isn't implemented natively.|Worst case scenario, hosted user data is found in contravension of GDPR regulation, incurring heavy fines.|4|4|Ensure hashing and data encryption is implemented before data is passed to the SQL server.|
|1.2.2|Flask sql iteration|Flasks handling of mySQL commands requires reliable data structure.|Worst case scenario, repeated mySQL errors thrown due to column incompatability.|3|3|Restructure database to ensure compatability errors are dodged or excepted.|
|1.3.1|Jenkins pipeline integration|Jenkins compatability with GitHub webhooks.|Worst case scenario builds are not triggered, resulting in inconsistent builds.|3|1|Maintain webhooks and pull/push requests, ensure branches merged correctly.|
|1.3.2|Jenkins server exposed.|Port 8080 open to webtraffic is poor working practice.|Worst case scenario, introduce systemic vulnerabilities into build server.|5|3|Investigated ngrok as port tunelling service, impractical for small scale project.|

## Project Architecture

### Entity Relationships

![The entity relationship diagram for the project, comprising the recipe, ingredients, and recipe_ingredients tables, and the unimplemented user table](https://i.imgur.com/XbLKyPc.png)

The core of the project comprises three linked tables, two main and one joining, in a mySQL database. The joining table links data from recipe and ingredients tables to show which ingredients are used in the methods for particular recipes. This architecture reduces the load that would be required for multiple empty fields for recipes as different recipes have different numbers of ingredients used for them.

Ancilliary to this are the user and admin tables, which aren't required to be instituted for project completion. This being said, they represent two different use cases for site approach. In terms of security and database management, they would have different permission roles and security provisions vis a vis the database itself, and most aspects of site architecture. As marks for this project are weighted toward backend technologies, as of project handoff, they have not been implemented.

To represent these options more clearly, I have included a use case diagram.

### Overall Architecture

![The architecture diagram for the project, showing an overview of the languages and toolsets used to build, control, test, and deploy.](https://i.imgur.com/5quYapC.png)

The project, known currently as ChilliApp, was built on a framework of python, with the use of the module Flask, and its extensions mysql_db and WTForms. The website displays using the Bootstrap API, with custom HTML and CSS stylings making use of Jinja2. Fully CRUD functional, it links to a mySQL server hosted on a GCP instance.

Version controlled by way of GitHub, the project uses a WebHook to toggle Jenkins pipeline builds. This CI/CD server can be obfuscated by way of ngrok to prevent port exposure, but this was not kept for the project handover, as the free version hangs the terminal.

The pipeline itself is coded in Groovy, making heavy use of BASH scripts to enable environment setup on the same GCP compute instance as the Jenkins server for testing.

Testing itself is achieved using PyTest and the Selenium plugin for flask, discussed later.

The finished build, if tests are passed, is deployed onto a worker node, where it launches using GUnicorn, at 6 nodes, to achieve poll stable load balancing.

### Issues Encountered

+ Swapped out SQLAlchemy for mysql_db.

+ Serious difficulties getting WTForms to take dynamic fields.

+ Used NGROK for port tunnelling until finding limitations of free version.

+ Ran into a lot of user permissions errors with Jenkins, studied the documentation

+ Ran into polling issues with GUnicorn

## Design Considerations

### Front End

Front end issues were not a focus for this project.

That being said, the bootstrap template was overridden in places with custom CSS stylings, and Jinja2 was used to inherit styling from the master layout template, and handle python form data objects for display.

### Back End

Agile principles of functional code over documentation and prioritisation of working builds lead to a pursuit of lowest path of resistance design.

App routes and functions in the project are prioritised to be multi function, using the variance of polled form data to determine data endpoints. An example programmatic flow chart is included for reference.

![Flow chart demonstrating process flow for the mvp page POST request handling stream](https://i.imgur.com/fHCiX9z.png)

Code representation:

```if request.method == "POST":
        details = request.form
        if "new_name" in details:
            recipe_name = details["recipe_name"]
            new_name = details["new_name"]
            cur = mysql.connection.cursor()
            cur.execute("UPDATE recipes SET recipe_name = (%s) WHERE recipe_name = (%s);", (new_name, recipe_name))
        elif "ingredient_name" in details:
            ingredient_name = details["ingredient_name"]
            cur = mysql.connection.cursor()
            cur.execute("SELECT id FROM ingredients WHERE ingredient_name = (%s)", [ingredient_name])
            ingredient_id = cur.fetchall()
            mysql.connection.commit()
            cur.execute("DELETE IGNORE FROM recipe_ingredients WHERE ingredient_id = (%s);", [ingredient_id])
            mysql.connection.commit()
            cur.execute("DELETE FROM ingredients WHERE ingredient_name = (%s);", [ingredient_name])
        else:
            recipe_name = details["recipe_name"]
            cur = mysql.connection.cursor()
            cur.execute("SELECT id FROM recipes WHERE recipe_name = (%s)", [recipe_name])
            recipe_id = cur.fetchall()
            mysql.connection.commit()
            cur.execute("DELETE IGNORE FROM recipe_ingredients WHERE recipe_id = (%s);", [recipe_id])
            mysql.connection.commit()
            cur.execute("DELETE FROM recipes WHERE recipe_name = (%s);", [recipe_name])
        mysql.connection.commit()
        cur.close()
        return redirect("/browse")
```

A mix of WTForms and HTML form POST handling was used to avoid substantial issues with Dynamic Form handling in mysql_db integration.

To prevent SQL conflicts, the mySQL instance data structure was chosen quite carefully. Examples of this would be the paired usage of IGNORE statements and UNIQUE keywords, to prevent col return errors.

Display of the database on the /browse page required careful understanding of the return structure of read data. A three table join was used to ensure that ingredients were linked to their correct recipes, and a nested set of for loops enables their handling and restructuring for Jinja display.

### UI

Beyond native bootstrap stylings, UI considerations were not at the forefront. Submissions boxes are selected to allow clear display and entry of data. Although the website itself is suited to wide aspect display and updated browsers, it still displays on phone browsers with minimal errors.

For the favicon, and placeholder branding design, a logo was created.

![ChilliApp Logo](https://i.imgur.com/8S5k1lK.gif)

## Testing

### Pytest

There are two main branches within the Pytest testing stream; url_testing, and db_testing.

Each of these are reflected in a separate stage within the Jenkinsfile pipeline instructions.

+ **url_testing**

The URL testing block pings each of the web pages in turn after a build to ensure that the site is up and callable, then verifies the results by pinging an absent 'negative' page.

7 tests are run.

1 for each page.

1 for an empty call.

Due to the complexity of called modules, coverage hovers around 46%.

+ **db_testing**

The database testing block spins a mirrored set of the mySQL tables in a separate database 'testing' on the instance. The database is wiped, and then each aspect of CRUD functionality is tested, mirroring the SQL structure of the flask functions.

17 tests are run.

The database is wiped.

Each table is CREATED, then checked for structure.

Each table is INSERTED into, then the UNIQUE keyword is tested.

Each table has a database entry UPDATED.

The FOREIGN KEY constraints are tested, before all entries are clean deleted.

Coverage averages 38%.

### Selenium

Selenium testing pending HTML [id] assignment.

### Final Report

Testing log stored on Jenkins server. Problems were encountered attempting to get the server to return testing documents to GitHub. It would be necessary to store GitHub login files as environmental variables on the server, which will be avoided for the project build. Currently the server is vulnerable to port mapping and injection, so account details will not be stored.

## Deployment

### Toolset

As of 2020/03/19.

+ GCP Instance development environment

+ GitHub Webhook

+ Jenkins Server

+ Pipeline build coded in Groovy and Shell.

+ Testing in Pytest using the Coverage module.

+ ~Front end testing in Selenium.~ [Not cooperating with mysql_db, fix pending]

+ 2 build run using debug mode and a GUnicorn 6 node mirror.

+ Final build deployment onto separate instance (currently inactive due to cost).

### CI Server Implementation

A jenkins server runs pipeline builds of the project, automating the testing functions, before deploying the website.

### Branch and Merge Log

Placeholder: polled Developer branch on 2020/03/19

```* commit a5b08b4a12ddac692300c130054ca9b4f7ff425f (HEAD -> developer, origin/developer)
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 14:37:21 2020 +0000
| 
|     source abandoned
| 
* commit ddbc9a565c685353ce359fd2b98759e7e6646443
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 14:24:31 2020 +0000
| 
|     source move
| 
* commit 911d4a7dcd2344365f37ee1c3c562c6a3997d36e
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 14:21:37 2020 +0000
| 
|     source move
| 
* commit 206869c302553dfb6c2104995c2f93d2f5cd77c2
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 14:18:48 2020 +0000
| 
|     source testing
| 
* commit 53f4376e6ef00d0d31058af8971d7bec1188fe5d
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 12:23:28 2020 +0000
| 
|     test test
| 
* commit 16dc6771da62cafd9954b6d35ff1296bb9ba0834
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 12:21:35 2020 +0000
| 
|     -m test
| 
* commit a90c43d886440424fe352eedca5426c84eb967e3
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 12:19:57 2020 +0000
| 
|     -m test
| 
* commit bb7d9ee8feec8fbaa3d08cc387f10e97a0a75ae3
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 12:15:07 2020 +0000
| 
|     Jenkins test
| 
* commit 2e76ea5fde8967cab20daa523244c00f674e11a3
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 12:09:40 2020 +0000
| 
|     restructure
| 
* commit ca672a1ebcb00800e9c14039ff7eef2067d2ac9a
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 19 12:04:26 2020 +0000
| 
|     chilli_app
```
(import of project from [ChilliAppTemp](https://github.com/THC-QA/ChilliFlaskAppTemp/tree/dev))
```
| 
* commit b8ff427ce85ae7059fa253730ec30fc56b00d4a1
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Thu Mar 19 11:33:53 2020 +0000
| 
|     Wrote up design considerations
| 
* commit 59eba8cf0bf6959f5d847181f9d1c3880cf715be
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Wed Mar 18 17:13:38 2020 +0000
| 
|     Architecture Diagram
| 
* commit 2a35459613c7b4c1c8dd34b07401da03bc8eadd3
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Wed Mar 18 09:48:02 2020 +0000
| 
|     Update
| 
* commit 4a8e632a112a786d99e454895fb8f3c8255d648e
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Mon Mar 16 17:16:58 2020 +0000
| 
|     Update README.md
| 
* commit cda1ded1e73fc6ade873aae1b76f40f94348e5a5
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Fri Mar 13 15:11:02 2020 +0000
| 
|     Rolling progress and Risk Assessment
|   
*   commit fed0b25a6720f70c28044a11bc214355dc9e98aa
|\  Merge: 47ef287 dc639bc
| | Author: THC-QA <Tristan.Clapp@academytrainee.com>
| | Date:   Fri Mar 13 10:57:10 2020 +0000
| | 
| |     Merge branch 'developer' of https://github.com/THC-QA/QA_SFIA_Project into developer
| |     
| |     JUST BECAUSE
| | 
| * commit dc639bcecfac0abfde6445c18b12ee64e28278a6
| | Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| | Date:   Wed Mar 11 16:24:18 2020 +0000
| | 
| |     Rolling and Risks
| | 
* | commit 47ef2875908c2da026496c47984ab1d38d693cda
|/  Author: THC-QA <Tristan.Clapp@academytrainee.com>
|   Date:   Fri Mar 13 10:56:55 2020 +0000
|   
|       UNIQUE KEY CONSTRAINTS
| 
* commit 41d5d2c0ada42f271e4a1f4d998c72c231556ef0
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Mar 6 15:28:57 2020 +0000
| 
|     Code despace update
| 
* commit 1c154bcc212669d38652a381603c0cd8dd92d0ec
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Mar 5 16:29:36 2020 +0000
| 
|     Fixed sql
|   
*   commit ba0449538824a09e8baeed8e465e51e333915fc3
|\  Merge: 2f1d8d2 7ad42b0
| | Author: THC-QA <Tristan.Clapp@academytrainee.com>
| | Date:   Wed Mar 4 16:40:27 2020 +0000
| | 
| |     Merge branch 'developer' of https://github.com/THC-QA/QA_SFIA_Project into developer
| | 
| * commit 7ad42b002ec6b409cabffa0014cc57066d6b2b1c
| | Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| | Date:   Tue Mar 3 15:31:34 2020 +0000
| | 
| |     Written up basic entity relationship introduction.
| | 
| * commit ddef18c969929ff54dbfa6204a5c712fb91bf84e
| | Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| | Date:   Tue Mar 3 13:27:51 2020 +0000
| | 
| |     Fixed formatting
| | 
| * commit ead51aa3c889f70f79742494b2b25e0dc475cabc
| | Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| | Date:   Mon Mar 2 18:13:18 2020 +0000
| | 
| |     Update README.md
| | 
* | commit 2f1d8d2e8e3e4d4d19646989e80d48444e6e4c13
|/  Author: THC-QA <Tristan.Clapp@academytrainee.com>
|   Date:   Wed Mar 4 16:35:39 2020 +0000
|   
|       Updated mySQL
| 
* commit e740fe75a6d93f7f4de4337550946a16a0ff4300
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Mon Mar 2 17:53:25 2020 +0000
| 
|     mySQL update.
| 
* commit a7adf4be85f8cd83cf8565f71e94f2c4bd83e37b
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Mon Mar 2 17:45:32 2020 +0000
| 
|     Completed mySQL initialisation file.
| 
* commit 2297099ff4eadfa181dd61d23040b25110962997
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Mon Feb 24 18:46:27 2020 +0000
| 
|     Updated changelog and risk assessment
| 
* commit 4b9d12356517ce8d45f7affd901b49309a35390e
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Fri Feb 21 10:55:55 2020 +0000
| 
|     date update
| 
* commit 2fc45af655a77a4f3f784b687aad95d4db51f1a4
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Fri Feb 21 10:55:16 2020 +0000
| 
|     Table experiment failed
| 
* commit 973943fd4836e7e1605c51b1dd9de981566ed8f0
| Author: THC-QA <61196018+THC-QA@users.noreply.github.com>
| Date:   Fri Feb 21 10:54:32 2020 +0000
| 
|     Update README.md
| 
* commit 917600983f811a0de8fdf9074b972bf2bfa72dd8
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:48:00 2020 +0000
| 
|     fixed?
| 
* commit e0f28dc7742db3370f75bd42c8f5be12d9af8684
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:45:41 2020 +0000
| 
|     and again...
| 
* commit 2472390b73f334795c20c478a2e21b4f09492cc0
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:31:20 2020 +0000
| 
|     try again
| 
* commit e0212ecf20c71c2020a668fe65de33325ef0776c
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:29:47 2020 +0000
| 
|     link fix 2
| 
* commit 8665ce52c4d682bf89e974a61b005c48c233b31b
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:27:52 2020 +0000
| 
|     link fix
| 
* commit 969baf54918f1018371335ad499729197aaa9b2f
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:26:21 2020 +0000
| 
|     ToC test
| 
* commit bc0302cab2f8cbb27aacfa7f834019d9aa86fcc3
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:15:14 2020 +0000
| 
|     updated risk assessment table
| 
* commit 46128b2997c1b296616c249a5fe6930971be18dc
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Fri Feb 21 10:08:24 2020 +0000
| 
|     added rolling changes to Trello
| 
* commit c689a4ecb7477dad7fb046faf55127dbf059370c
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 17:33:57 2020 +0000
| 
|     table update
| 
* commit 84a96192a85edfb008f77877685cb0727ed2a8e3
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 17:27:16 2020 +0000
| 
|     Table formatting fixed?
| 
* commit 3080e1b9b54e1c4b64c3af0362291b3a4129f239
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 17:24:18 2020 +0000
| 
|     Initialise risk assessment.
| 
* commit 0350be076670ca6eb17e823ec13b638b6300e22a
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 11:33:47 2020 +0000
| 
|     fix formatting
| 
* commit 8a3652a16ce5e29d04776ff2b5f50149ca3a1881
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 11:31:02 2020 +0000
| 
|     continued headings.
| 
* commit a0e6ff3aab28b69887d07f3db4d5d53bfc80c4af
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 10:52:43 2020 +0000
| 
|     Fixed linking
| 
* commit 0415d7c844918a6cd6491655d22f13da53d09756
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Thu Feb 20 10:48:36 2020 +0000
| 
|     Updated Trello explanation, removed selenium.
| 
* commit 6da12824011b4199feda8ed1b49ba7a9d8bc7aad
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 18:52:01 2020 +0000
| 
|     final fix on nested lists, remember four spaces
| 
* commit 1f2e748bf83b9b383a430d8991d9a9822eec6023
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 18:49:15 2020 +0000
| 
|     fixed image linking to direct link
| 
* commit a00646525c1a7716acbd6a69bdbabf043c070fd1
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 18:47:20 2020 +0000
| 
|     Sub-lists not working, check tomorrow.
| 
* commit b6948ea0c40d74a892a5bdfae83ebb84fa8b611b
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 18:42:40 2020 +0000
| 
|     Documentation formatting fix for ToC (spaces)
| 
* commit b971c4c91681a0f404eb2daff361167fc96a95df
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 18:39:04 2020 +0000
| 
|     Documentation formatting fix for ToC
| 
* commit ffbf55c5c183ac718d8a329db976c259299d0768
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 18:36:34 2020 +0000
| 
|     Start of formal documentation for project.
| 
* commit 4cd1fc1214c6df89ecd8a042216a70fc1c9b3967
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 16:41:03 2020 +0000
| 
|     Dev branch created - test
| 
* commit 7666a1441144553ce4209fa561c8cbf1fbc5f4d0
| Author: THC-QA <Tristan.Clapp@academytrainee.com>
| Date:   Wed Feb 19 15:31:52 2020 +0000
| 
|     Second update.
| 
* commit ee7f918b96524284fd8c9d50638aa82aa8363990
  Author: THC-QA <Tristan.Clapp@academytrainee.com>
  Date:   Wed Feb 19 15:14:38 2020 +0000
  
      Test file README from THC
(END)
```

## Front End Considerations

Taking industry standards into consideration, the lack of a single native page webApp, and the lack of coherent use of Javascript, and JQuery means there is substantial room for improvement in the front end of the website. Limited time meant that the usage of Bootstrap was clumsy at best, even as a shortcut.

Site functionality itself could be improved, particularly in regards to a search function, and full coverage for user accounts and Admin/Moderator privileges.

Documentation was severely lacking for WTForms, Coverage, and other modules, as they are presupposing very specific setups and project architecture. Whilst the usage of mysql_db over SQLAlchemy was far more intuitive, and makes better use of non-native mySQL servers, its support and documentation is minimal, and Alchemy seems to be the more popular option.

The industry is increasingly moving to coherent, single window, modular webApps, and for an enterprise project, it would be necessary to follow the skills sets for the industry. Some more distributed formats suit the code structure of a python back end relation, a noteable example being Reddit.

For future considerations, particularly regarding the usage of python as a web development language, [Aaron Swartz's views](http://www.aaronsw.com/weblog/rewritingreddit) on migrating large services, and the lack of decent API development, it will be necessary to keep a tight eye on the open source community, and its reactions to industry demands.

## Improvements for Future Versions

In addition to front end considerations, an enterprise version of the app would require a change in the deployment and testing cycle.

Even before thinking about containerisation or distribution of core functionalities, the current exposure of various ports would have to be 
#### Authors

#### Acknowledgements
