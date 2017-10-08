.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
  select seven,image from students;

CREATE TABLE smallest_int AS
  select time,smallest from students where smallest>5
    order by smallest limit 20;

CREATE TABLE greatstudents AS
  select su.date,su.color,su.pet,su.number,sp.number
  from students as su,sp17students as sp
  where su.date=sp.date and su.color=sp.color and su.pet=sp.pet;

CREATE TABLE sevens AS
  select seven from students,checkboxes
  where number=7 and checkboxes."7"='True' and students.time=checkboxes.time;

CREATE TABLE matchmaker AS
  select sua.pet,sua.beets,sua.color,sub.color from students as sua,students as sub
  where sua.time<sub.time and sua.pet=sub.pet and sua.beets=sub.beets;
