ThinGit
=======

Sounds Funny, What is It?
-------

Ever use Thingiverse? MyMiniFactory? Cults3d?

They offer you a way to search through models, find pictures and descriptions, and otherwise easily navigate the many files that are out there.

Then there's that folder on your computer with various zips, sub-folders, and many random STLs. Which was the good benchy STL again?

ThinGit (pronounced "thing, it" or "thin, git" depending on how you want to say it) allows for turning that mess of a folder into an orginized and personal 3D model repository.

How?
----

TBD

Can I Deploy This?
----

TBD

What's Needed?
----

Generally, a computer running Python 3.7+

Requirements:

- Python 3.7
- Pipenv

Plans
----

TBD (move to a different file?)

1. Simple, probably CLI model index (STL, 3MF, ZIP, 7z, RAR), make DB so indexing doesn't need to happen often (source data, dest gcode, dates?). This will probably get vastly expanded...
2. Website where you can actually browse the lists of models (images, turn arounds, etc.) [Flutter? Or was that only on mobile]
3. Collections, likes, etc.
4. Assembly (thank you [Autodrop3D](https://www.autodrop3d.com/) for the concept) so multi-part models can be handled as one large model
5. Offline browsing (be able to export a collection or whole thing as a HTML archive so people can look at it who aren't running/able to connect to server)
6. Sourcing (where did the model come from) / pull info from source / can I go to another site through this and downloads auto-add them to my collection? (maybe likes and collections can translate through too)
7. Remix/Fork support
8. Revisions/branches (like Git) so changes to models can be tracked
9. {redacted} ;)
10. Collabroative modeling? (epitamy of "git", but also allow for specialized access so individuals (or groups) can access certain models but no one else. This is perfect for Kickstarter groups to enable access sets of models + people purchasing models and getting acces [purchasing API is to be done on your own, not this project])
11. Integrate with other services/systems? (allow other web servers to simply forward requests to this + iframe or similar... basically just writing docs/examples for doing this)
12. REST API (for when someone doesn't want #11 and instead wants their own UI, have a REST API that people can use/access)

Random:

* Some point support online deployments?
* Scaling?
* API?
* Accounts?
* Requests?
* Don't want to go too crazy with this: initial intent was "how do I show people what models I have?"

License
----

MIT (see LICENSE file)

CoC
----

TBA (To Be Added)
