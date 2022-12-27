# ExcelData_API_Filter

This is the Given [Dataset](https://docs.google.com/spreadsheets/d/1z9ioyt1v-BtpOn7BK8WGL76zuO9UKJWQ0G-tiS-_zvg/edit#gid=0) that we need to Normalize into  database Table.

The Given Query are:

1.  Create a post API to upload all the projects from sheet into database
2.  Create an API to list the projects and apply filters (sector, ministry, project status, date,
etc.)
3.  Create an API which shows the summary data of the project (project count, total budget,
sector wise project count and budget). This api should use all the filters you created in the
step 1 and change accordingly) 
<br>

    Expected Output of Qn.3:
    {
    "project_count": 111,
    "total_budget": 495121847,
    "sector": [
    {
    "id": 1,
    "name": "Health",
    "project_count": 31,
    "budget":12123213
    },
    {
    "id": 2,
    "name": "Agriculture",
    "project_count": 31,
    "budget":12123213
    },
    {
    "id": 3,
    "name": "Education",
    "project_count": 16,
    "budget":12123213
    }]
    }
<br>
4.  Create another api to count the number of projects and budgets (municipality wise and
district wise). Apply province and district filters too
<br>

    Expected output of Qn.4 : [
    {
    "id": 1924,
    "name": "Kalika Gaunpalika",
    "count": 12,
    "budget":12344,
    },
    {
    "id": 1925,
    "name": "Khandachakra Nagarpalika",
    "count": 8,
    "budget":12344,
    },
    {
    "id": 1926,
    "name": "Mahawai Gaunpalika",
    "count": 7,
    "budget":12344
    }
    ]
    
