import json
from datetime import datetime
from django.http import JsonResponse
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue

def reporters(request):
    if request.method=='POST':
        try:
            data=json.loads(request.body)
            r=Reporter(**data); r.validate()
            reporters=json.load(open('reporters.json'))
            reporters.append(r.to_dict())
            json.dump(reporters,open('reporters.json','w'))
            return JsonResponse(r.to_dict(),status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=400)

    if request.method=='GET':
        reporters=json.load(open('reporters.json'))
        rid=request.GET.get('id')
        if rid:
            for r in reporters:
                if r['id']==int(rid): return JsonResponse(r)
            return JsonResponse({'error':'Reporter not found'},status=404)
        return JsonResponse(reporters,safe=False)

    if request.method=='PUT':
        data=json.loads(request.body)
        reporters=json.load(open('reporters.json'))
        for i in range(len(reporters)):
            if reporters[i]['id']==data.get('id'):
                reporters[i].update(data)
                json.dump(reporters,open('reporters.json','w'))
                return JsonResponse(reporters[i])
        return JsonResponse({'error':'Reporter not found'},status=404)

    if request.method=='DELETE':
        rid=int(request.GET.get('id'))
        reporters=json.load(open('reporters.json'))
        new=[r for r in reporters if r['id']!=rid]
        json.dump(new,open('reporters.json','w'))
        return JsonResponse({'message':'deleted'})


def issues(request):
    if request.method=='POST':
        try:
            data=json.loads(request.body)
            if data['priority']=='critical':
                issue=CriticalIssue(**data)
            elif data['priority']=='low':
                issue=LowPriorityIssue(**data)
            else:
                issue=Issue(**data)
            issue.validate()
            d=issue.to_dict()
            d['created_at']=str(datetime.now())
            d['message']=issue.describe()
            issues=json.load(open('issues.json'))
            issues.append(d)
            json.dump(issues,open('issues.json','w'))
            return JsonResponse(d,status=201)
        except Exception as e:
            return JsonResponse({'error':str(e)},status=400)

    if request.method=='GET':
        issues=json.load(open('issues.json'))
        iid=request.GET.get('id')
        status=request.GET.get('status')
        if iid:
            for i in issues:
                if i['id']==int(iid): return JsonResponse(i)
            return JsonResponse({'error':'Issue not found'},status=404)
        if status:
            return JsonResponse([i for i in issues if i['status']==status],safe=False)
        return JsonResponse(issues,safe=False)

    if request.method=='PUT':
        data=json.loads(request.body)
        issues=json.load(open('issues.json'))
        for i in range(len(issues)):
            if issues[i]['id']==data.get('id'):
                issues[i].update(data)
                json.dump(issues,open('issues.json','w'))
                return JsonResponse(issues[i])
        return JsonResponse({'error':'Issue not found'},status=404)

    if request.method=='DELETE':
        iid=int(request.GET.get('id'))
        issues=json.load(open('issues.json'))
        new=[i for i in issues if i['id']!=iid]
        json.dump(new,open('issues.json','w'))
        return JsonResponse({'message':'deleted'})
