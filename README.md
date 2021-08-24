# Getting Started

1. Create and activate virtual environment
2. Run `pip install -r requirements.txt`
3. Run `flask db init`
4. Run `flask db migrate -m "user table"`
5. Run `flask db migrate -m "proverb table"`
6. Run `flask db upgrade`
7. Run `flask run`
   `WARNING: some pages are styled by Bootstrap, so you need internet ,otherwise the pages may look like ugly or incomprehensible.`

# References

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask WTF](https://flask-wtf.readthedocs.io/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [demo authentication](https://github.com/innomadic/flask_authentication_demo)
- [Mega Tutorial](https://github.com/innomadic/flask_authentication_demo)
- [databases](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
- [delete items from database](https://www.youtube.com/watch?v=w_VHabMAM1c)
- [updating items ](https://github.com/innomadic/todo_web/tree/main/app)
- [basic commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)

# Lessons Learned

In day one, everything was easy I've created proverb form and listed it, I've learned how to commit and push in Git using command lines.

In day two, as usually life don't give two good days, it was hard for me to update and delete items from database in the web app and it takes seven hours to do this(nearly whole of my progamming day, and then discover it's not required).

In day three, I learned how to limit maximum length and return error user try to submit above limit length. I've learned too what is current.user and created about page(nearly finished).

the project was fun and easy but the hardest part was connecting between tables, making relational database.

finaly, I learned :

- How to update items
- and delete items from database
- basic git commands
- styling flask templates
