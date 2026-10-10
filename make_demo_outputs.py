"""Generate transparent, deterministic illustrative fixtures (not LLM responses)."""
from pathlib import Path
import json

ROOT = Path(__file__).parent
cv = json.loads((ROOT/'sample_data/synthetic_candidate_cv.json').read_text(encoding='utf-8'))
job = (ROOT/'sample_data/sample_job_description.txt').read_text(encoding='utf-8')
reqs = job.split('Requirements\n',1)[1].split('\nResponsibilities\n',1)[0].strip().splitlines()
resps = job.split('Responsibilities\n',1)[1].split('\nDisclaimer:',1)[0].strip().splitlines()
reqs = [r[2:] for r in reqs if r.startswith('- ')]
resps = [r[2:] for r in resps if r.startswith('- ')]
assert len(reqs)==9 and len(resps)==7
categories=['education','business_analysis','technical','business_analysis','business_analysis','methodology','technical','technical','soft_skills']
extract={
 'status':'OK',
 'job_metadata':{'job_title':'Senior Business Analyst','employer':'Example Enterprise Solutions (fictional)','recruiter':None,'location':'Istanbul, Türkiye','work_model':'Hybrid','source_url':None,'extraction_date':'2026-10-10'},
 'requirements':[{'id':f'REQ-{i:03d}','text':t,'category':categories[i-1],'priority':'UNSPECIFIED','source_section':'Requirements','source_item_index':i,'source_evidence':t} for i,t in enumerate(reqs,1)],
 'responsibilities':[{'id':f'RESP-{i:03d}','text':t,'source_section':'Responsibilities','source_item_index':i,'source_evidence':t} for i,t in enumerate(resps,1)],
 'validation':{'requirements_count':9,'responsibilities_count':7,'unverifiable_fields':['recruiter','source_url'],'warnings':['Synthetic job posting; no explicit requirement priorities']}}

# Evidence quotations are exact substrings of the public synthetic Markdown CV.
quotes=[
 ('Education','BSc, Computer Science'),
 ('Professional Experience','Modeled as-is and to-be processes using BPMN'),
 ('Professional Experience','Used SQL queries to validate data flows and prepare operational reports.'),
 ('Professional Experience','documented functional and non-functional requirements.'),
 ('Professional Experience','wrote user stories, use cases, and acceptance criteria for two Scrum teams.'),
 ('Core Skills','Agile/Scrum, SDLC'),
 ('Professional Experience','Analyzed REST API and web-service integration scenarios'),
 ('Professional Experience','evaluated potential AI-assisted workflow improvements.'),
 ('Professional Experience','Facilitated stakeholder meetings and communicated implementation trade-offs.')]
cv_md=(ROOT/'sample_data/synthetic_candidate_cv.md').read_text(encoding='utf-8')
for sec,quote in quotes: assert quote in cv_md,quote
matrix=[]
for i,(section,quote) in enumerate(quotes,1):
 matrix.append({'requirement_id':f'REQ-{i:03d}','cv_only_status':'MATCHED','confirmed_status':'MATCHED','evidence_strength':'STRONG' if i in (1,2,3,4,5,7) else 'MODERATE','evidence':[{'source_type':'CV_DOCUMENTED','source_section':section,'exact_quote':quote,'user_confirmation_date':None}],'gap':'','suggested_revision':'','human_review_required':False})
matching={'status':'OK','matching_matrix':matrix,'scoring':{'scoring_rule':{'MATCHED':1,'PARTIALLY_MATCHED':0.5,'NOT_VERIFIABLE':0,'NOT_MATCHED':0},'requirement_count':9,'cv_only_alignment_percent':100.0,'confirmed_alignment_percent':100.0,'official_ats_score':None},'validation':{'all_requirement_ids_present':True,'warnings':['Illustrative synthetic case; 100% is a rubric alignment score, not an ATS score.']}}
summary=('Senior Business Analyst with 10 years of experience in fictional financial services, telecom, and cloud software environments. '
 'Experienced in eliciting and documenting business requirements, mapping processes with BPMN, and creating user stories and use cases. '
 'Hands-on exposure to SQL-based validation, REST API and web-service integration scenarios, and system integration testing. '
 'Comfortable working in Agile teams and coordinating user acceptance testing with business stakeholders and development teams. '
 'Interested in responsible applications of AI-assisted workflow improvement and evidence-based delivery practices. '
 'Brings cross-functional communication and analytical problem-solving skills to complex enterprise initiatives.')
assert 80<=len(summary.split())<=120
bullet='Analyzed REST API and web-service integration scenarios, including field mappings and error handling, for a cloud operations platform.'
letter=('Dear Hiring Team,\n\n'
 'I am applying for the Senior Business Analyst position at Example Enterprise Solutions. My background spans business analysis roles in fictional cloud software, financial services, and telecommunications environments. I am particularly interested in a role that combines requirements engineering, process improvement, data analysis, and cross-functional delivery.\n\n'
 'At Northstar Cloud Systems, I documented functional and non-functional requirements for a cloud operations platform. I modeled current and future processes using BPMN, prepared user stories and use cases, and supported two Scrum teams. I also analyzed REST API and web-service integration scenarios, including field mappings and error handling. These experiences are relevant to your focus on integration design and clear communication with development teams.\n\n'
 'My work also included SQL-based data validation, system integration testing, and coordination of user acceptance testing. Earlier roles involved functional specifications, process diagrams, and stakeholder workshops. I have also evaluated potential AI-assisted workflow improvements, while recognizing that practical applications require human review and appropriate controls.\n\n'
 'I would welcome the opportunity to discuss how this experience could support your business analysis and product improvement priorities. Thank you for your consideration.\n\nSincerely,\nAlex Morgan')
assert 180<=len(letter.split())<=260,len(letter.split())
claims=[
 ('CLM-001','Computer Science degree',['REQ-001'],quotes[0]),
 ('CLM-002','BPMN process modeling',['REQ-002'],quotes[1]),
 ('CLM-003','SQL data validation and reporting',['REQ-003'],quotes[2]),
 ('CLM-004','Functional and non-functional requirements documentation',['REQ-004'],quotes[3]),
 ('CLM-005','User stories, use cases, acceptance criteria and Scrum teamwork',['REQ-005','REQ-006'],quotes[4]),
 ('CLM-006','REST API and web-service integration scenarios',['REQ-007'],quotes[6]),
 ('CLM-007','Evaluated AI-assisted workflow improvements',['REQ-008'],quotes[7]),
 ('CLM-008','Stakeholder communication',['REQ-009'],quotes[8]),
 ('CLM-009','System integration testing and UAT',['REQ-007'],('Professional Experience','Coordinated system integration testing and user acceptance testing, tracking defects through resolution.')),
 ('CLM-010','10 years of experience',['REQ-002'],('Professional Summary','Senior Business Analyst with 10 years of fictional experience')),
 ('CLM-011','Financial services and telecommunications experience',['REQ-002'],('Professional Summary','financial services, telecommunications, and cloud software')),
 ('CLM-012','Agile/Scrum and SDLC',['REQ-006'],quotes[5]),
 ('CLM-013','Field mappings and error handling',['REQ-007'],('Professional Experience','including field mappings and error handling.'))]
for _,_,_,(_,q) in claims: assert q in cv_md,q
trace=[{'claim_id':cid,'claim_text':claim,'requirement_ids':ids,'evidence_source':'CV_DOCUMENTED','source_section':s,'exact_quote_or_confirmation':q,'confirmation_date':None} for cid,claim,ids,(s,q) in claims]
content={'status':'OK','draft_status':'DRAFT — HUMAN APPROVAL REQUIRED','professional_summary':summary,'core_skills':['Business Analysis','Requirements Engineering','BPMN','SQL','Data Analysis','Functional Analysis','User Stories','Use Cases','Agile/Scrum','SDLC','REST APIs','Web Services','Integration Testing','UAT','Stakeholder Management','AI Workflow Evaluation'],'experience_revisions':[{'original_role':'Senior Business Analyst | Northstar Cloud Systems (fictional)','proposed_bullet':bullet,'claim_ids':['CLM-006','CLM-013']}],'cover_letter':letter,'claim_traceability':trace,'human_review_flags':['Illustrative output authored from synthetic inputs, not produced by an LLM run.','Review wording and all material claims before external use.'],'submission_authorized':False}
qa={'status':'OK','validation_status':'REVIEW','structural_validation':{'passed':True,'issues':[]},'claim_audit':[{'claim_id':x['claim_id'],'classification':'CV_DOCUMENTED','verified':True,'source_reference':f"synthetic_candidate_cv.md / {x['source_section']}: {x['exact_quote_or_confirmation']}",'issue':None} for x in trace],'quality_scores':{'factual_accuracy':5,'evidence_traceability':4,'job_relevance':5,'ats_friendly_structure':4,'writing_quality':4,'human_approval_safety':5,'weighted_total_out_of_100':90.0},'issues':['Manual QA review is still required; rubric values are illustrative, not independently audited.'],'recommended_corrections':['Review the synthetic letter and evidence coverage before publishing as a demonstrated example.'],'human_approval':{'status':'PENDING','approved_version':None,'checklist':['Verify all claims against synthetic source','Review drafts','Approve exact final version']},'submission_authorized':False}
# weighted score: 25+20+20+8+8+10 =91
qa['quality_scores']['weighted_total_out_of_100']=91.0
for name,obj in [('01_requirements.json',extract),('02_cv_matching.json',matching),('03_application_draft.json',content),('04_quality_validation.json',qa)]:
 (ROOT/'outputs'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated four JSON demo artifacts; all quoted CV evidence verified.')
