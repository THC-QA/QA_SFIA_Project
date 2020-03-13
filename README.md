# README
---
# Hot Sauce Recipe Database
---
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
5. Design Considerations
    + Front End
    + Back End
    + UI
6. Testing
    + Pytest Testing
    + Postman Testing
    + Final Report
7. Deployment
    + Toolset
    + CI Server Implementation
    + Branch and Merge Log
8. Front End Implementation
9. Improvements for Future Versions
+ Authors
+ Acknowledgements

## Project Brief
---

### Proposal

## Trello Board
---

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

### End Point

## Risk Assessment
---

|Risk No.|Risk|Description|Hazard|Likelihood|Impact|Solution|
|---|---|---|---|---|---|---|
|1.0.1|Overrun on time.|Due to poor time management, the project is not completed.|Worst case scenario, marks are lost due to lack of coverage of brief.|2|5|Make good use of Kanban to manage workflow, and efficient time use of office resources.|
|1.0.2|Data breach on workstation.|Due to accident or malicious action, workstation is compromised.|Worst case scenario, severe progress loss.|1|5|Change passwords on workstation, keep e-services logged off when not in use.|
|1.1.1|Overrunning on GCP free data limits.|An instance is left running, or an account breach enables the resources on the account to be drained.|Worst case scenario, databases are unaccessable.|1|5|Continue monitoring GCP usage. Copy databases offline as final backup.|
|1.1.2.1|Database security: SQL|The GCP server is breached in some way, compromising data integrity.|Worst case scenario, data is lost, or user data is compromised.|3|5|Ensure user and personal data is encrypted, and passwords hashed, before being moved to the database.|
|1.1.2.2|Database security: SSH|Unmanaged connections cause data leak or damage, keys are lost or stolen.| Worst case scenario, GDPR noncompliance or total data compromisation.|2|5|Learn and make use of GCP's SSH key management role system, and implement it correctly.|
|1.1.2.3|Database security: SQL-I|Unsanitised user input allows SQL injection into the database.|Worst case scenario, database is maliciously destroyed.|2|5|Ensure any user accessible inputs are sanitised, and implement permission roles.|
|1.2.1|Flask password storage|Although Flask uses passwords fields, hashing isn't implemented natively.|Worst case scenario, hosted user data is found in contravension of GDPR regulation, incurring heavy fines.|4|4|Ensure hashing and data encryption is implemented before data is passed to the SQL server.|

## Project Architecture
---

### Entity Relationships

The core of the project comprises three linked tables, two main and one joining, in a mySQL database. The joining table links data from recipe and ingredients tables to show which ingredients are used in the methods for particular recipes. This architecture reduces the load that would be required for multiple empty fields for recipes as different recipes have different numbers of ingredients used for them.

Ancilliary to this are the user and admin tables, which aren't required to be instituted for project completion. This being said, they represent two different use cases for site approach. In terms of security and database management, they would have different permission roles and security provisions vis a vis the database itself, and most aspects of site architecture.

To represent this more clearly, I have included use case diagram.

### Overall Architecture

### Issues Encountered
