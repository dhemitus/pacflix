#!/usr/bin/env python3

from user import User
from plan import Plan
from userplan import Userplan
from db import user_data
from db import plan_data
from db import user_plan
from db import DB

if __name__ == "__main__":

    # initiate db
    db = DB(user_data, plan_data, user_plan)

    #initiate user instance
    user = User(db.user)

    print("\n\n---get user by name-------------------------")
    cahya = user.get_userbyname("cahya")
    print(cahya)

    print("\n\n---get user by id---------------------------")
    shandy = user.get_userbyid(1)
    print(shandy)

    print("\n\n---add new user-----------------------------")
    anon = user.add_user("Toni")
    print(anon)
    toni = user.get_userbyname("toni")
    print(toni)
    tono = user.add_user("tono")
    print(tono)


    print("\n\n---get all users----------------------------")
    print(user.get_alluser())

    #initiate plan instance
    plan = Plan(db.plan)

    print("\n\n---get plan by name-------------------------")
    basic = plan.get_planbyname("basic plan")
    print(basic)

    print("\n\n---get plan by id---------------------------")
    premium = plan.get_planbyid(3)
    print(premium)
    
    print("\n\n---add new plan-----------------------------")
    nplan = plan.add_plan("Exclusive Plan", "True", "True", ["SD", "HD", "UHD", "UUHD"], 8, "Premium Plan + foreign movie", 240_000)
    print(nplan)
    exc = plan.get_planbyname("exclusive plan")
    print(exc)

    print("\n\n---get all plans----------------------------")
    print(plan.get_allplan())

    #initiate user plan instance
    userplan = Userplan(db.userplan, user.data, plan.data)

    print("\n\n---get user plan----------------------------")
    pcahya = userplan.get_userplan(cahya)
    print(userplan.plan)
    print(pcahya)

    print("\n\n---add new user plan------------------------")
    print("---invalid user-----------------------------")
    nshandy = userplan.add_userplan(shandy, basic, 'ana-2134')
    print(nshandy)

    print("---invalid refferal-------------------------")
    ntoni = userplan.add_userplan(toni, basic, 'toni-2134')
    print(ntoni)
    ntoni = userplan.add_userplan(toni, basic, 'toni-1234')
    print(ntoni)

    print("--------------------------------------------")
    ntoni = userplan.add_userplan(toni, basic, 'ana-2134')
    print(ntoni)


    print("\n\n---upgrade user plan------------------------")
    print("---unregistered upgrad----------------------")
    unreg = userplan.upgrade_userplan(tono, basic)
    print(unreg)

    print("---invalid upgrade--------------------------")
    inv = userplan.upgrade_userplan(cahya, basic)
    print(inv)

    print("--------------------------------------------")
    valt = userplan.upgrade_userplan(cahya, premium)
    print(valt)

    print("\n\n---get all users plan-----------------------")
    print(userplan.data)
    print(userplan.get_alluserplan())
