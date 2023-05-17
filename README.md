# What is Alembic?
1. Lightweight database migration tool for when using SQLAlchemy.
2. Migration tools allow us to plan, transfer and upgrade resources within databases.
3. Alembic allows you to change a SQLAlchemy database table after it has been created.

# Using Alembic
1. Installation: `pip install alembic`
2. Initialize a new, generic environment: `alembic init <folder_name>`
3. Create a new revision of the environment: `alembic revision -m <message>`
4. Run our upgrade migration to our database: `alembic upgrade <revision #>`
5. Run our downgrade migration to our database: `alembic downgrade <revision #>`

# Alembic.ini file
1. Has configuration for alembic.
2. Is the file that alembic looks for when invoked.

# Alembic Directory
1. Has all environmental properties for Alembic.
2. Holds all revisions of our application.
3. Where you call migrations for upgrading and downgrading.

# What is Jinja?
1. Fast, expressive and extensible templating language.
2. Able to write code similar to Python in the DOM.
3. The template is passed data to render within the final document.

# What is Render?
1. Platform as a Service (PaaS) and Code deployment service.
2. Helps developers build, run and operate applications entirely on the cloud.
3. Developers can focus on coding and not have to worry about the infrastructure of their applications.
4. Has a Free Trial/Free Tier.

# Create a requirements.txt file
On the terminal, run command ```pip freeze > requirements.txt```