declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"guides": {
"en/check-turkish-e-invoice.md": {
	id: "en/check-turkish-e-invoice.md";
  slug: "en/check-turkish-e-invoice";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/check-turkish-trade-registry-gazette.md": {
	id: "en/check-turkish-trade-registry-gazette.md";
  slug: "en/check-turkish-trade-registry-gazette";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/checklist-before-paying-turkish-supplier.md": {
	id: "en/checklist-before-paying-turkish-supplier.md";
  slug: "en/checklist-before-paying-turkish-supplier";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/coordinate-factory-supplier-visit.md": {
	id: "en/coordinate-factory-supplier-visit.md";
  slug: "en/coordinate-factory-supplier-visit";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/documents-to-request-turkish-supplier.md": {
	id: "en/documents-to-request-turkish-supplier.md";
  slug: "en/documents-to-request-turkish-supplier";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/due-diligence-turkish-company.md": {
	id: "en/due-diligence-turkish-company.md";
  slug: "en/due-diligence-turkish-company";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/interpreter-international-business-meetings.md": {
	id: "en/interpreter-international-business-meetings.md";
  slug: "en/interpreter-international-business-meetings";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/overseas-supplier-red-flags.md": {
	id: "en/overseas-supplier-red-flags.md";
  slug: "en/overseas-supplier-red-flags";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/practical-business-assistance-turkiye.md": {
	id: "en/practical-business-assistance-turkiye.md";
  slug: "en/practical-business-assistance-turkiye";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/prepare-before-contacting-supplier.md": {
	id: "en/prepare-before-contacting-supplier.md";
  slug: "en/prepare-before-contacting-supplier";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/prepare-business-visit-supplier.md": {
	id: "en/prepare-business-visit-supplier.md";
  slug: "en/prepare-business-visit-supplier";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/public-records-limitations.md": {
	id: "en/public-records-limitations.md";
  slug: "en/public-records-limitations";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/supplier-factory-verification-turkiye.md": {
	id: "en/supplier-factory-verification-turkiye.md";
  slug: "en/supplier-factory-verification-turkiye";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/turkish-supplier-warning-signs.md": {
	id: "en/turkish-supplier-warning-signs.md";
  slug: "en/turkish-supplier-warning-signs";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/turkiye-business-verification-resources.md": {
	id: "en/turkiye-business-verification-resources.md";
  slug: "en/turkiye-business-verification-resources";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-business-documents.md": {
	id: "en/verify-business-documents.md";
  slug: "en/verify-business-documents";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-mersis-registration.md": {
	id: "en/verify-mersis-registration.md";
  slug: "en/verify-mersis-registration";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-overseas-supplier-existence.md": {
	id: "en/verify-overseas-supplier-existence.md";
  slug: "en/verify-overseas-supplier-existence";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-turkish-company-address.md": {
	id: "en/verify-turkish-company-address.md";
  slug: "en/verify-turkish-company-address";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-turkish-company-representative.md": {
	id: "en/verify-turkish-company-representative.md";
  slug: "en/verify-turkish-company-representative";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-turkish-company.md": {
	id: "en/verify-turkish-company.md";
  slug: "en/verify-turkish-company";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"en/verify-ukrainian-company.md": {
	id: "en/verify-ukrainian-company.md";
  slug: "en/verify-ukrainian-company";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"tr/fabrika-ziyareti-hazirligi.md": {
	id: "tr/fabrika-ziyareti-hazirligi.md";
  slug: "tr/fabrika-ziyareti-hazirligi";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"tr/ukrayna-sirket-sorgulama.md": {
	id: "tr/ukrayna-sirket-sorgulama.md";
  slug: "tr/ukrayna-sirket-sorgulama";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"tr/yurtdisi-tedarikci-dogrulama.md": {
	id: "tr/yurtdisi-tedarikci-dogrulama.md";
  slug: "tr/yurtdisi-tedarikci-dogrulama";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"uk/perevirka-turetskoyi-kompaniyi.md": {
	id: "uk/perevirka-turetskoyi-kompaniyi.md";
  slug: "uk/perevirka-turetskoyi-kompaniyi";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"uk/perevirka-zavodu-v-turechchyni.md": {
	id: "uk/perevirka-zavodu-v-turechchyni.md";
  slug: "uk/perevirka-zavodu-v-turechchyni";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
"uk/pidhotovka-do-vizytu-na-zavod.md": {
	id: "uk/pidhotovka-do-vizytu-na-zavod.md";
  slug: "uk/pidhotovka-do-vizytu-na-zavod";
  body: string;
  collection: "guides";
  data: InferEntrySchema<"guides">
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		"countries": {
"turkiye": {
	id: "turkiye";
  collection: "countries";
  data: InferEntrySchema<"countries">
};
"ukraine": {
	id: "ukraine";
  collection: "countries";
  data: InferEntrySchema<"countries">
};
};
"tools": {
"iran-compliance": {
	id: "iran-compliance";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"russia-compliance": {
	id: "russia-compliance";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"turkiye-ivd": {
	id: "turkiye-ivd";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"turkiye-mersis": {
	id: "turkiye-mersis";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"turkiye-ticaret-sicil": {
	id: "turkiye-ticaret-sicil";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"turkiye-turkpatent": {
	id: "turkiye-turkpatent";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"ukraine-opendatabot": {
	id: "ukraine-opendatabot";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"ukraine-usr": {
	id: "ukraine-usr";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
"ukraine-youcontrol": {
	id: "ukraine-youcontrol";
  collection: "tools";
  data: InferEntrySchema<"tools">
};
};

	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = typeof import("../../src/content/config.js");
}
